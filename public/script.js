// State Management for the Map and Data
let map;
let allHubsData = []; // Caches the full dataset from your API (2848 records)
let activeMarkers = []; // Tracks current map pins so we can clear them dynamically

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

        allHubsData = hubs; // Cache the raw data for later filtering and marker management

        // TASK 2.1: Cache the data locally and create markers
        allHubsData = hubs.map(hub => {
            // Failsafe: Ensure the hub actually has coordinates before drawing
            if (!hub.lat || !hub.lng) return hub;

            // Calculate a rough size multiplier based on athletes
            const scaleSize = Math.min(15, Math.max(5, hub.athletes / 5));
            
            // Create the markers
            const marker = new google.maps.Marker({
                position: { lat: parseFloat(hub.lat), lng: parseFloat(hub.lng) },
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

            // Click listener for Gemini insight
            marker.addListener('click', () => {
                fetchHubData(hub.city, hub.state);
            });

            // Save the marker instance INSIDE the hub object
            hub.marker = marker; 
            return hub;
        });

        // TASK 2.2: Build the menu (assuming you have your hardcoded function)
        populateSportsDropdown();        


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
            <div align="left">
                <h2 style="color: #1a73e8;">${data.stats.city}, ${data.stats.state}</h2>
                
                <div class="stat-box bg-blue"><strong>Athletes:</strong> ${data.stats.total_athletes}</div>
                <div class="stat-box bg-red"><strong>Medals:</strong> ${data.stats.total_medals}</div>

                <h3 style="color: #5f6368;">Dominant Sports</h3>
                <p>${data.stats.clustered_sports}</p>

                <h4 style="color: #1a73e8;">Gemini Enterprise Agent Platform Insight</h4>
                <div class="insight-text">${paragraphs}</div>
            </div>
        `;
    } catch (error) {
        console.error("Fetch failed:", error);
        // THIS PREVENTS THE INFINITE HANGING TEXT ISSUE BY DISPLAYING AN ERROR MESSAGE INSTEAD
        contentArea.innerHTML = `<p style='color:red;'>Error fetching data for ${cityName}. Error: ${error.message}</p>`;
    }
}


// --- TASK 2.2: Hard-Coded Sports Dropdown ---
function populateSportsDropdown() {
    const dropdown = document.getElementById('sport-filter');
    
    // Clear the dropdown and add the default "All Sports" option first
    dropdown.innerHTML = '<option value="all">All Sports</option>';

    // Hard-coded list from TeamUSA.com CSV
    const teamUsaSports = [
        "Alpine Skiing", "Archery", "Artistic Swimming", "Badminton", "Baseball", 
        "Basketball", "Biathlon", "Blind Soccer", "Bobsled", "Boccia", "Bowling", 
        "Boxing", "Breaking", "Canoe/Kayak", "Cross-Country Skiing", "Curling", 
        "Cycling", "Diving", "Equestrian", "Fencing", "Field Hockey", "Figure Skating", 
        "Freestyle Skiing", "Goalball", "Golf", "Gymnastics", "Ice Hockey", "Judo", 
        "Karate", "Luge", "Nordic Combined", "Para Alpine Skiing", "Para Archery", 
        "Para Judo", "Para Nordic Skiing", "Para Powerlifting", "Para Shooting", 
        "Para Snowboarding", "Para Swimming", "Para Table Tennis", "Para Taekwondo", 
        "Para Track and Field", "Para-Badminton", "Para-Cycling", "Para-Equestrian", 
        "Para-Rowing", "Paracanoe", "Paratriathlon", "Pentathlon", "Racquetball", 
        "Roller Sports", "Rowing", "Rugby", "Sailing", "Shooting", "Sitting Volleyball", 
        "Skateboarding", "Skeleton", "Ski Jumping", "Ski Mountaineering", "Sled Hockey", 
        "Snowboarding", "Soccer", "Soccer 7-A-Side", "Softball", "Speedskating", 
        "Sport Climbing", "Squash", "Surfing", "Swimming", "Table Tennis", "Taekwondo", 
        "Team Handball", "Tennis", "Track and Field", "Triathlon", "Volleyball", 
        "Water Polo", "Water Ski/Wakeboard", "Weightlifting", "Wheelchair Basketball", 
        "Wheelchair Curling", "Wheelchair Fencing", "Wheelchair Rugby", "Wheelchair Tennis", 
        "Wrestling"
    ];

    // Loop through the array and append each sport as an option
    teamUsaSports.forEach(sport => {
        const option = document.createElement('option');
        option.value = sport; // Make sure your BigQuery data matches this exact string
        option.textContent = sport;
        dropdown.appendChild(option);
    });
}


// 4. Filter Map by Sport (High Performance Version)
document.getElementById('sport-filter').addEventListener('change', (event) => {
    // 1. Normalize the user's selection to lowercase
    const selectedSport = event.target.value.toLowerCase().trim();
    const showAll = (selectedSport === 'all' || selectedSport === 'all sports');

    // 2. Loop through our permanent data vault
    allHubsData.forEach(hub => {
        // FIX: Add safety check in case a hub object failed to map correctly
        if (!hub) return;

        let isMatch = showAll;

        // Ensure the hub has the clustered_sports property before trying to read it
        if (!showAll && hub.clustered_sports) {
            // Force BigQuery data into a lowercase string for safe comparison
            const sportsData = String(hub.clustered_sports).toLowerCase();
            isMatch = sportsData.includes(selectedSport);
        }

        // 3. Toggle visibility
        if (hub.marker) {
            hub.marker.setVisible(isMatch);
        }
    });
});




// Expose initMap to the global window object so the Google Maps script tag can call it
window.initMap = initMap;