let map;

// 1. Initialize the Google Map
async function initMap() {
    map = new google.maps.Map(document.getElementById("map-container"), {
        center: { lat: 39.8283, lng: -98.5795 }, // Center of USA
        zoom: 4,
        mapId: "HOMETOWNSUCCESS"
    });

    // 2. Fetch all hubs from your Python backend
    try {
        const response = await fetch("https://hometown-success-engine-583694496401.us-west2.run.app/api/hubs");

        const hubs = await response.json();
        
        // 3. Loop through the hubs and drop a pin for each
        hubs.forEach(hub => {
            // Calculate a rough size multiplier based on athletes
            const scaleSize = Math.min(15, Math.max(5, hub.athletes / 5));

            const marker = new google.maps.Marker({
                position: { lat: hub.lat, lng: hub.lng },
                map: map,
                title: hub.city,
                icon: {
                    path: google.maps.SymbolPath.CIRCLE,
                    scale: scaleSize,
                    fillColor: "#1a73e8",
                    fillOpacity: 0.8,
                    strokeColor: "#ffffff",
                    strokeWeight: 1
                }
            });

            // 4. Listen for clicks on the pins
            marker.addListener("click", () => {
                fetchHubData(hub.city, hub.state);
            });
        });
    } catch (error) {
        console.error("Error loading initial hubs:", error);
        document.getElementById("content-area").innerHTML = "<p style='color:red;'>Make sure your Python server is running!</p>";
    }
}

// 5. Fetch Gemini Enterprise Agent Platform data when a pin is clicked
async function fetchHubData(cityName, stateName) {
    const contentArea = document.getElementById("content-area");
    contentArea.innerHTML = `<h3>Analyzing ${cityName}...</h3><p>Consulting Gemini Enterprise Agent Platform...</p>`;

    const queryCity = encodeURIComponent(cityName);
    const queryState = encodeURIComponent(stateName);

    try {
        const response = await fetch(`https://hometown-success-engine-583694496401.us-west2.run.app/api/hub/${queryCity}/${queryState}`);
        const data = await response.json();

        // Check if Gemini failed to return the insight
        if (!data.insight) {
             throw new Error("Missing Gemini insight data");
        }

        // Format the AI narrative paragraphs
        const paragraphs = data.insight.split('\n\n').map(p => `<p>${p}</p>`).join('');

        // Update the sidebar with the new data
        contentArea.innerHTML = `
            <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-align: left;">
                <h1 style="color: #1a73e8; margin-top: 0;">${data.stats.city}, ${data.stats.state}</h1>
                
                <div class="stat-box bg-blue"><strong>Athletes:</strong> ${data.stats.total_athletes}</div>
                <div class="stat-box bg-red"><strong>Medals:</strong> ${data.stats.total_medals}</div>

                <h4 style="color: #5f6368; margin-bottom: 5px;">Dominant Sports</h4>
                <p style="margin-top: 0; font-weight: 500;">${data.stats.clustered_sports}</p>

                <h4 style="border-bottom: 2px solid #1a73e8; padding-bottom: 5px; margin-top: 30px;">Gemini Enterprise Agent Platform Insight</h4>
                <div class="insight-text">${paragraphs}</div>
            </div>
        `;
    } catch (error) {
        console.error("Fetch failed:", error);
        // THIS PREVENTS THE INFINITE HANGING TEXT ISSUE BY DISPLAYING AN ERROR MESSAGE INSTEAD
        contentArea.innerHTML = `<p style='color:red;'>Error fetching data for ${cityName}. Error: ${error.message}</p>`;
    }
}
