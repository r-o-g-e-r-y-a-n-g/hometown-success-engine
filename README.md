# Hometown Success Engine for Team USA

**Explore athlete hometowns across sports on our interactive map with Gemini.**

[![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)](https://cloud.google.com/)
[![BigQuery](https://img.shields.io/badge/BigQuery-4285F4?style=for-the-badge&logo=google-bigquery&logoColor=white)](https://cloud.google.com/bigquery)
[![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black)](https://firebase.google.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
![Google Gemini](https://img.shields.io/badge/google%20gemini-8E75B2?style=for-the-badge&logo=google%20gemini&logoColor=white)

---

## 🌎 Overview
Where can we find athletic success? Our project maps 7,800 Team USA athletes across 2,800 hometowns. We correlate geography with sports using Gemini to reveal how America fosters Team USA excellence.
### 🏆 Key Features
- **Sports Filtering:** *Filter Map by Sport* to find athlete hubs for your favorite sport!
- **Integrated Architecture:** We built on Google Cloud for speed and use advanced markers to provide city info. Responsive UI/UX with Old Glory Blue markers that turn Old Glory Red on hover. A ‘Gold Medal Rim’ signifies that the city has medalists.
- **Artificial Intelligence:** Geographic Information Systems (GIS) meets Gemini. Interactively generate a story about a city’s dominant sports. Learn from AI insights about geography, climate, altitude, mountains, bodies of water, and sports facilities.

---

## 🖥️ Architecture
This project is a full-stack application built using **Google Cloud Platform**:
* **Database:** **Google BigQuery** securely stores and queries our custom geocoded Team USA datasets.
* **Backend:** A fast Python **Flask** server deployed via **Google Cloud Run** supports our application.
* **Frontend:** HTML & JavaScript interactive dashboard on **Google Maps Platform**, served globally with **Firebase Hosting**.
* **AI:** **Gemini Enterprise Agent Platform** processes city athlete statistics and highlights geographic features to generate sports narratives.

---

## 📝 Reproducible Testing Instructions
The best way to evaluate the Hometown Success Engine is via our live deployment, which integrates our Google BigQuery dataset and Gemini Enterprise Agent Platform.
1. Navigate to the Live Site: Open [HometownSuccess.com](https://hometownsuccess.com) in any modern web browser. The Hometown Success Engine is hosted on Firebase.
2. Explore this map for Team USA: You will see a Google Map populated with city markers. The number on the markers corresponds to the count of Team USA athletes from that specific city. Formatting of the circle with a gold rim indicates that the city has medalists.
3. Filter the All Sports default map and select a specific sport to evaluate by clicking the dropdown menu. The map API will update to show a subset of cities from the complete dataset, and individual cities will be easier to select.
4. Trigger the Gemini AI Engine: Click on any of the city markers (e.g., Colorado Springs, CO which is the location of the U.S. Olympic & Paralympic Training Center).
5. Evaluate the AI Insight: The side-panel will refresh displaying the city statistics including number of Team USA athletes, dominant sports, and a dynamically generated Gemini Enterprise Agent Platform Insight. Review this text to see how the Gemini model correlates Team USA athlete statistics and local geography to generate inclusive sports narratives.


*⚠️ Note on Local Testing & GitHub Forking: This code repository relies on a private BigQuery instance and Google Cloud Platform API keys.*
If you wish to deploy this architecture yourself, you must:
1. Create a Google Cloud Project and enable the BigQuery, Maps, and Gemini API.
2. Upload athlete data to your own BigQuery dataset.
3. Update the app.py queries to point to your new dataset.
4. Create a .env file in the root directory and add: GEMINI_API_KEY=your_key_here.

---

## 🧰 Hometown Success Engine Tech Stack Video
In this video, we break down the technology stack and data flow that powers our interactive mapping platform. Click the preview to watch on YouTube.

[![Hometown Success Engine Tech Stack Video](https://img.youtube.com/vi/2rn3J4Ln5oU/0.jpg)](https://www.youtube.com/watch?v=2rn3J4Ln5oU)

---

## ✅ Development Notes

2026-05-09: We're now using AdvancedMarkerElement in Google Maps API. If you visited our site before this update and see blue markers of different sizes on the map, you will need to empty cache for your browser and do a hard reload of hometownsuccess.com (CTRL+SHIFT+R). If you see circles with numbers in them, those are AdvancedMarkerElements in Google Maps and you are viewing our most recent version. A hard reload of the browser will refresh the JavaScript cache & CSS styles for the site.


## 🇺🇸🥇🥈🥉⚽🏀🎾🏐🏓🏸⛳🏉🤾🏑🏃🤸🏋️🏹🤺🥋🤼🥊🎯
**Built by [Roger Yang](https://www.linkedin.com/in/rogeryang1/) & [Gemini](https://gemini.google.com/) for the [Team USA x Google Cloud Hackathon](https://vibecodeforgoldwithgoogle.devpost.com/).**
## 🏊🤽🚣🛶⛵🏄🚴🚵🛹🧗🏇⛷️🎿🏂⛸️🏒🥌🛷🧑‍🦽🧑‍🦼🦯🕺💃
