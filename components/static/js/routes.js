
   document.addEventListener("DOMContentLoaded", function () {
  // 🎨 Fixed colors for each jeepney
  const jeepneyColors = [
    "#1E88E5", // Blue
    "#43A047", // Green
    "#E53935", // Red
    "#FB8C00", // Orange
    "#8E24AA", // Purple
  ];

  // 🗺️ Initialize map
  const map = L.map("map", {
    maxBounds: [
      [10.63, 122.45],
      [10.83, 122.65],
    ],
    maxBoundsViscosity: 1.0,
  }).setView([10.7202, 122.5621], 12);

  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: "© OpenStreetMap contributors",
  }).addTo(map);

  // 📋 Get jeepney data
  const jeepneysData = document.getElementById("jeepList").dataset.jeepneys;
  const jeepneys = JSON.parse(jeepneysData);

  const routeLayers = {};
  const legendDiv = document.getElementById("legend");
  const showAllBtn = document.getElementById("showAllBtn");

  // 🚍 Draw routes
  jeepneys.forEach((jeep, index) => {
    if (jeep.start_lat && jeep.start_lng && jeep.end_lat && jeep.end_lng) {
      const color = jeepneyColors[index % jeepneyColors.length];

      const route = L.Routing.control({
        waypoints: [
          L.latLng(jeep.start_lat, jeep.start_lng),
          L.latLng(jeep.end_lat, jeep.end_lng),
        ],
        addWaypoints: false,
        draggableWaypoints: false,
        fitSelectedRoutes: false,
        show: false,
        lineOptions: {
          styles: [{ color, weight: 5, opacity: 0.9 }],
        },
        createMarker: () => null,
      }).addTo(map);

      routeLayers[jeep.jeepney_name] = route;

      // 🟩 Add legend item
      const legendItem = document.createElement("div");
      legendItem.classList.add("legend-item");
      legendItem.innerHTML = `
        <div style="display:flex;align-items:center;gap:8px;cursor:pointer;">
          <div class="color-box" style="background:${color}"></div>
          <span>${jeep.jeepney_name}</span>
        </div>
      `;

      legendItem.addEventListener("click", () => {
        Object.values(routeLayers).forEach((r) => map.removeControl(r));
        route.addTo(map);
      });

      legendDiv.insertBefore(legendItem, showAllBtn);
    }
  });

  // 🟦 Show all button
  showAllBtn.addEventListener("click", () => {
    Object.values(routeLayers).forEach((r) => r.addTo(map));
  });

  // 🟨 Jeep list click
  document.querySelectorAll(".jeep-item").forEach((item) => {
    item.addEventListener("click", () => {
      const name = item.dataset.jeep;
      Object.values(routeLayers).forEach((r) => map.removeControl(r));
      if (routeLayers[name]) routeLayers[name].addTo(map);
    });
  });

  // Show all on load
  Object.values(routeLayers).forEach((r) => r.addTo(map));
});
