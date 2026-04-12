# 🏅 Hometown Success Engine 🇺🇸

**An Interactive AI-Powered Map Exploring the Geography of Team USA Excellence.**

## 🇺🇸🥇🥈🥉⚽🏀🎾🏐🏓🏸⛳🏉🤾🏑🏃🤸🏋️🏹🤺🥋🤼🥊🎯

[![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)](https://cloud.google.com/)
[![Gemini](https://img.shields.io/badge/Vertex_AI_Gemini-8E75B2?style=for-the-badge&logo=google-gemini&logoColor=white)](https://cloud.google.com/vertex-ai)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black)](https://firebase.google.com/)

---

## 🌎 The Vision
The **Hometown Success Engine** illuminates the relationship between the American landscape and the development of Team USA athletes. By correlating official Olympic and Paralympic data with geographic locations, this tool visually maps "Athlete Hubs" across the country.

Instead of just showing statistics, the Engine utilizes **Google Vertex AI** to dynamically generate inclusive, conditional narratives explaining how a region's unique geography, climate, or infrastructure (e.g., coastal waters, mountain elevations, dense urban centers) can build strong athletic communities.
---
(353)
The **Hometown Success Engine** maps the hometowns of Team USA athletes across the USA. The United States of America has diverse terrain, climate, and infrastructure that can build strong athletic communities. Our tool visualizes how certain sports can cluster around "Athlete Hubs" across the country and could help find our next hometown success.

Instead of just showing statistics, the Engine utilizes **Google Vertex AI** to dynamically generate detailed narratives explaining how a region's unique geography, climate, or infrastructure provide the environment for Team USA excellence.
---

## 🖥️ Architecture
This project is a fully serverless, full-stack application built exclusively on the Google Cloud ecosystem:
* **Database:** **Google BigQuery** securely hosts and queries the geocoded Team USA dataset.
* **AI Engine:** **Google Vertex AI** processes hub statistics on the fly to generate nuanced, rule-compliant narratives.
* **Backend API:** A lightweight **Python Flask** server deployed via **Google Cloud Run** acts as the bridge.
* **Frontend:** A lightning-fast Vanilla HTML/JS interactive dashboard utilizing the **Google Maps Platform**, hosted globally on **Firebase Hosting**.

---

## 🚀 Live Demo
**[\[Hometown Success Engine\]](https://integral-zephyr-492520-b1.web.app/)**

*Tip: Click on any blue dot on the map to trigger the Vertex AI narrative!*

---

## 💻 Local Testing Instructions
You can easily spin this project up locally to test the BigQuery and Gemini API integrations.

### Prerequisites
1. Python 3.9+ installed.
2. The Google Cloud CLI installed and authenticated.
3. A Google AI Studio / Gemini API Key.

### Step 1: Clone the Repository
```Bash
git clone [https://github.com/YOUR_USERNAME/hometown-success-engine.git](https://github.com/YOUR_USERNAME/hometown-success-engine.git)
cd hometown-success-engine
```

### Step 2: Install Backend Dependencies
```Bash
pip install -r requirements.txt
```

### Step 3: Configure Environment Variables
Create a .env file in the root directory and add your Gemini API key:
```Plaintext
GEMINI_API_KEY="your_api_key_here"
```

Ensure your local environment is authenticated with Google Cloud to allow BigQuery access:
```Bash
gcloud auth application-default login
```

### Step 4: Start the Python Backend
Fire up the Flask API, which will connect to BigQuery and Vertex AI.
```Bash
python app.py
(The server will run on http://127.0.0.1:5000)
```

### Step 5: Launch the Interactive Map
Open a new terminal window, navigate to the public folder where the frontend code lives, and start a local web server:
```Bash
cd public
python -m http.server 8000
```
Open your web browser and navigate to http://localhost:8000. Click any hub on the map to see the Hometown Success Engine in action!

## 🏊🤽🚣🛶⛵🏄🚴🚵🛹🧗🏇⛷️🎿🏂⛸️🏒🥌🛷🧑‍🦽🧑‍🦼🦯🕺💃

**🤝 Designed and engineered by Roger Yang with Gemini 3 for the Team USA x Google Cloud Hackathon.**