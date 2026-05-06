# Hometown Success Engine for Team USA

**An interactive map exploring the hometowns of Team USA athletes with Gemini.**

[![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)](https://cloud.google.com/)
[![BigQuery](https://img.shields.io/badge/BigQuery-4285F4?style=for-the-badge&logo=google-bigquery&logoColor=white)](https://cloud.google.com/bigquery)
[![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black)](https://firebase.google.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
![Google Gemini](https://img.shields.io/badge/google%20gemini-8E75B2?style=for-the-badge&logo=google%20gemini&logoColor=white)

---

## 🌎 Overview
How do we find elite athletes? Every sports champion starts somewhere. Have you ever wondered if the place you live shapes the athlete you become? Do local mountains build better snowboarders? Do wide-open plains forge faster runners? We built the Hometown Success Engine to find out. By mapping over 8,000 elite Team USA athletes across 3,000 cities, we visualize how geography influences athletic development. Our Gemini AI engine then analyzes the hidden connections between local weather, landscapes, and specific sports. Our vision is to show how the American landscape fosters Team USA excellence.

---

## 🖥️ Architecture
This project is a full-stack application built using Google Cloud Platform:
* **Database:** **Google BigQuery** securely hosts and queries the geocoded Team USA dataset.
* **Backend:** A lightweight **Python Flask** server deployed via **Google Cloud Run** acts as the bridge.
* **Frontend:** HTML/JS interactive dashboard using **Google Maps Platform**, hosted globally on **Firebase Hosting**.
* **AI Engine:** **Gemini Enterprise Agent Platform** processes hub statistics on the fly to generate sports narratives.

---

## 📝 Reproducible Testing Instructions
The easiest way to evaluate the Hometown Success Engine is via our live deployment, which is fully wired to our Google BigQuery dataset and Gemini Enterprise Agent Platform.

1. Navigate to the Live Site: Open [HometownSuccess.com](https://hometownsuccess.com) in any modern web browser. The [Hometown Success Engine](https://hometown-success-engine.firebaseapp.com) is hosted on Firebase.

2. Explore the Spatial Data: You will see a Google Map populated with hubs. The size of the markers correlates to the volume of Team USA athletes from that specific region.

3. Trigger the Gemini AI Engine: Click on any of the blue hub markers (e.g., Colorado Springs, CO which is the location of the U.S. Olympic & Paralympic Training Center).

4. Evaluate the AI Insight: A side-panel will open displaying the number of Team USA athletes, their top clustered sports, and a dynamically generated Gemini Enterprise Agent Platform Insight. Review this text to see how the Gemini model correlates the local geography/climate to the dominant sports using conditional, inclusive phrasing.

---

*⚠️ Note on Local Testing: This application relies on a private Google BigQuery instance and Gemini Enterprise Agent Platform API keys.*

If you wish to deploy this architecture yourself, you must:

1. Create a Google Cloud Project and enable the BigQuery and Gemini AI APIs.

2. Upload athlete data to your own BigQuery dataset.

3. Update the app.py queries to point to your new dataset.

4. Create a .env file in the root directory and add: GEMINI_API_KEY=your_key_here.

## Hometown Success Engine Tech Stack Video

In this video, we break down the technology stack and data flow that powers our interactive mapping platform. Click the preview to watch on YouTube.

[![Hometown Success Engine Tech Stack Video](https://img.youtube.com/vi/2rn3J4Ln5oU/0.jpg)](https://www.youtube.com/watch?v=2rn3J4Ln5oU)


## 🇺🇸🥇🥈🥉⚽🏀🎾🏐🏓🏸⛳🏉🤾🏑🏃🤸🏋️🏹🤺🥋🤼🥊🎯
**Designed and engineered by Roger Yang with Gemini for the Team USA x Google Cloud Hackathon.**
## 🏊🤽🚣🛶⛵🏄🚴🚵🛹🧗🏇⛷️🎿🏂⛸️🏒🥌🛷🧑‍🦽🧑‍🦼🦯🕺💃
