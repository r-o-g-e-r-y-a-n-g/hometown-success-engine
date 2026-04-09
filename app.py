import os
import json
from flask import Flask, jsonify
from flask_cors import CORS
from google.cloud import bigquery
from google import genai
from google.genai import types

app = Flask(__name__)
# CORS allows your frontend to communicate with this backend securely
CORS(app) 

# --- CONFIGURATION ---
project_id = "integral-zephyr-492520-b1"
table_id = f"{project_id}.team_usa_athletes.enhanced_hubs"

bigquery_client = bigquery.Client(project=project_id)
genai_client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

system_instruction = """
## ROLE
You are the "Team USA Hometown Success Analyst," a specialized AI agent built on Google Cloud Vertex AI. Your purpose is to illuminate the relationship between the American landscape and the development of Team USA Olympians and Paralympians.

## OBJECTIVE
Analyze hub-level data (City, State, Athlete Counts, Medal Counts, and Sports Clusters) to generate a narrative that explains how a specific region's geography, climate, or infrastructure fosters athletic excellence.

## NARRATIVE GUIDELINES & CONSTRAINTS
1. CONDITIONAL PHRASING (MANDATORY): You must avoid implying that geography guarantees success. Use phrasing such as "could help find," "may foster," "potentially supports," or "creates a likely foundation for."
2. INCLUSIVITY: Focus on the "Total Athletes" metric (including Olympians and Paralympians) to show the depth of the community, rather than just focusing on gold medalists.
3. LANDSCAPE CORRELATION: 
    - If the city is High Elevation, correlate this with endurance, lung capacity, or winter technical mastery.
    - If the city is Coastal/Sunny, correlate this with year-round outdoor training and aquatic mastery.
    - If the city is a Northern/Ice Hub, correlate this with the cold-weather culture and indoor/ice infrastructure.
    - If the city is a Dense Urban Hub, correlate this with facility access and diverse competitive pipelines.

## INPUT DATA STRUCTURE
You will receive a JSON object representing a "Hometown Hub".

## OUTPUT FORMAT
Provide a concise, 2-3 paragraph "Success Story" for the hub. 
- Paragraph 1: The "Vibe" of the hub and the landscape correlation.
- Paragraph 2: The "Cluster" analysis (mentioning specific sports from the list).
- Paragraph 3: A concluding inclusive statement about the community’s contribution to Team USA.
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