import os
import json
from flask import Flask, jsonify
from flask_cors import CORS
from google.cloud import bigquery
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv() 

app = Flask(__name__)
# CORS allows your frontend to communicate with this backend securely
CORS(app) 

# --- CONFIGURATION ---
project_id = "integral-zephyr-492520-b1"
table_id = f"{project_id}.team_usa_athletes.enhanced_hubs"

bigquery_client = bigquery.Client(project=project_id)
genai_client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

system_instruction = """
# Team USA Hometown Success Engine - System Instructions

## ROLE & OBJECTIVE
You are the "Team USA Hometown Success Analyst," an AI dedicated to illustrating the connection between the American landscape, infrastructure, and the development of elite Team USA Olympians and Paralympians. Your core task is to analyze provided hub-level data to craft a compelling narrative explaining how a region's unique attributes foster athletic excellence.

## TONE & STYLE
Your narrative must be concise, impactful, and strictly limited to 250 words. The tone should be a motivational blend of a **sports coach** (encouraging, insightful about athletic potential) and a **travel agent** (evocative, highlighting unique regional features).

## CORE NARRATIVE PRINCIPLES

1.  **Probabilistic Language (MANDATORY):** Avoid definitive statements about guaranteed success. Use cautious, encouraging phrasing such as "could help find," "may foster," "potentially supports," or "creates a likely foundation for." Integrate these phrases naturally into sentences without additional punctuation.

2.  **Inclusivity Focus:** Emphasize the "total_athletes" metric (including both Olympians and Paralympians) to highlight the community's broad contribution and depth of talent, rather than solely focusing on medalists.

3.  **Landscape & Infrastructure Correlation:** Directly link the region's characteristics to athletic development:
    *   **High Elevation (e.g., Colorado Springs):** Correlate with enhanced endurance, lung capacity, physiological advantages, or winter technical mastery.
    *   **Coastal/Sunny (e.g., San Diego, Lake Forest):** Correlate with year-round outdoor training, aquatic sports mastery, or diverse terrain for conditioning.
    *   **Northern/Ice Hub (e.g., Lake Placid):** Correlate with cold-weather culture, ice sports infrastructure, or winter sports resilience.
    *   **Dense Urban Hub (e.g., Los Angeles, Chicago):** Correlate with extensive facility access, diverse competitive pipelines, and a large talent pool.
    *   **Specialized Niche (e.g., Boyds for Table Tennis, Acworth for Swimming):** Correlate with specific local clubs, natural resources (lakes), or focused coaching.

## INPUT DATA STRUCTURE
You will receive a JSON object representing a "Hometown Hub":
- `city` (string)
- `state` (string)
- `total_athletes` (int)
- `total_medals` (int)
- `clustered_sports` (string - comma separated list, indicating sports played by world-class Team USA athletes from this hub)

## OUTPUT FORMAT
Generate a "Hometown Success Story" structured into two concise paragraphs:

*   **Paragraph 1: Regional Introduction & Assets**
    *   Begin with "[city] in [state]", using the full name of the state.
    *   Highlight key geographic features and local climate appealing to athletes. Mention the specific numerical altitude of the city.
    *   Comment on prominent athletic facilities in the region and any additional facts interesting to Team USA users.

*   **Paragraph 2: Athletic Development & Conclusion**
    *   Correlate how the described environment nurtures competitive athletes, performing a cluster analysis that mentions specific elite-level sports from "clustered_sports".
    *   Analyze the hometown's propensity to produce elite athletes, maintaining an encouraging tone.
    *   Conclude with an inclusive statement about the community's overall contribution to Team USA, emphasizing "total_athletes".
"""

@app.route('/api/hub/<city_name>', methods=['GET'])
def get_hub_insight(city_name):
    """Fetches BigQuery data for a city, then generates a Gemini insight."""
    
    # 1. PULL DATA FROM BIGQUERY
    query_string = f"SELECT * FROM `{table_id}` WHERE city = @city LIMIT 1"
    job_config = bigquery.QueryJobConfig(
        query_parameters=[bigquery.ScalarQueryParameter("city", "STRING", city_name)]
    )
    query_job = bigquery_client.query(query_string, job_config=job_config)
    query_results = list(query_job.result())

    if not query_results:
        return jsonify({"error": f"Hub '{city_name}' not found."}), 404

    target_row = query_results[0]
    
    # 2. FORMAT THE PAYLOAD
    hub_data = {
        "city": target_row.city,
        "state": target_row.state,
        "total_athletes": target_row.total_athletes,
        "total_medals": target_row.total_medals,
        "clustered_sports": target_row.clustered_sports
    }
    json_payload = json.dumps(hub_data, indent=2)

    # 3. GENERATE VERTEX AI NARRATIVE
    model_name = "gemini-2.5-flash"
    generate_config = types.GenerateContentConfig(
        temperature=0.7,
        system_instruction=system_instruction,
    )
    
    prompt_contents = [
        types.Content(role="user", parts=[types.Part.from_text(text=json_payload)])
    ]
    
    try:
        genai_response = genai_client.models.generate_content(
            model=model_name,
            contents=prompt_contents,
            config=generate_config,
        )
        ai_narrative = genai_response.text
    except Exception as api_error:
        ai_narrative = f"Error generating AI insight: {api_error}"

    # 4. RETURN THE COMBINED DATA TO THE FRONTEND
    final_output = {
        "stats": hub_data,
        "latitude": target_row.latitude,
        "longitude": target_row.longitude,
        "insight": ai_narrative
    }
    
    return jsonify(final_output)

# FETCH COORDINATES FOR MAP
@app.route('/api/hubs', methods=['GET'])
def get_all_hubs():
    """Fetches just the coordinates and sizes to draw the initial map."""
    query_string = f"SELECT city, state, latitude, longitude, total_athletes FROM `{table_id}` WHERE latitude IS NOT NULL"
    query_job = bigquery_client.query(query_string)
    
    # Format the results for the React map
    hubs = []
    for row in query_job:
        hubs.append({
            "city": row.city,
            "state": row.state,
            "lat": row.latitude,
            "lng": row.longitude,
            "athletes": row.total_athletes
        })
    
    return jsonify(hubs)

if __name__ == '__main__':
    app.run(debug=True, port=5000)