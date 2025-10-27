let userLat, userLng;
    let map, routingControl;

    // Get user's location
    if ("geolocation" in navigator) {
      navigator.geolocation.getCurrentPosition((pos) => {
        userLat = pos.coords.latitude;
        userLng = pos.coords.longitude;
      });
    }

    // 🔍 Search location and display jeepneys
    async function searchLocation() {
      const query = document.getElementById("searchInput").value.trim();
      const resultsDiv = document.getElementById("results");
      resultsDiv.innerHTML = "🔎 Searching...";

      if (!query) {
        resultsDiv.innerHTML = "<p>Please enter a location first.</p>";
        return;
      }

      try {
        // Get coordinates of searched location
        const geoRes = await fetch(`https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(query)}`);
        const geoData = await geoRes.json();
        if (geoData.length === 0) {
          resultsDiv.innerHTML = "<p>Location not found.</p>";
          return;
        }
        const lat = parseFloat(geoData[0].lat);
        const lng = parseFloat(geoData[0].lon);

        // Fetch jeepneys from backend using lat/lng
        const res = await fetch(`/user/search?lat=${lat}&lng=${lng}`);
        const data = await res.json();

        if (!Array.isArray(data) || data.length === 0) {
          resultsDiv.innerHTML = "<p>No available jeepneys found near this location.</p>";
          return;
        }

        // Display jeepneys as buttons
        resultsDiv.innerHTML = "";
        data.forEach((jeep) => {
          const btn = document.createElement("button");
          btn.className = "jeep-btn";
          btn.innerHTML = `
            <strong>${jeep.jeepney_name}</strong> – ${jeep.route}<br>
            Fare: ₱${jeep.fare} | Distance: ${jeep.distance_km} km
          `;
          btn.onclick = () => openMapModal(lat, lng, jeep);
          resultsDiv.appendChild(btn);
        });
      } catch (err) {
        console.error(err);
        resultsDiv.innerHTML = "<p>⚠️ Error searching for jeepneys.</p>";
      }
    }

    // 🗺️ Open map modal and show route
    function openMapModal(destLat, destLng, jeep) {
      const modal = document.getElementById("mapModal");
      modal.style.display = "flex";

      // Initialize map if not yet created
      if (!map) {
        map = L.map("map").setView([destLat, destLng], 13);
        L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
          maxZoom: 19,
          attribution: "&copy; OpenStreetMap contributors"
        }).addTo(map);
      }

      // Remove previous route
      if (routingControl) map.removeControl(routingControl);

      // Add route from user location to jeepney’s location (or destination)
      routingControl = L.Routing.control({
        waypoints: [
          L.latLng(userLat, userLng),
          L.latLng(destLat, destLng)
        ],
        routeWhileDragging: true
      }).addTo(map);
    }

    // Close modal
    function closeModal() {
      document.getElementById("mapModal").style.display = "none";
      if (routingControl) map.removeControl(routingControl);
    }








    