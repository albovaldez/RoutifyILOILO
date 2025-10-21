function initMap() {
        const iloilo = {lat: 10.7202, lng: 122.5621};

        const map = new google.maps.Map(document.getElementById("map"),{
            zoom: 13,
            center: iloilo,
        });

        const routeCoordinates = [
            {lat: 10.7202, lng: 122.5621 },
            {lat: 10.7251, lng: 122.5689 },
            {lat: 10.7285, lng: 122.5710 },
        ];

        const jeepneyRoute = new google.maps.Polyline({
            path: routeCoordinates,
            geodesic: true,
            strokeColor: "#FF9900",
            strokeOpacity: 1.0,
            strokeWeight: 5,
        });

        jeepneyRoute.setMap(map);

        const stops = [
            {name: "Plaza Libertad", position: {lat: 10.7202, lng: 122.5621 } },
            {name: " Iloilo Business Park", position: {lat: 10.7251, lng: 122.5689} },
            {name: "SM City Iloilo", position:  {lat: 10.7285, lng: 122.5710 } },
        ];

        stops.forEach((stop)=> {
            const marker = new google.maps.Marker({
                positon: stop.position, 
                map,                       
                title: stop.name,
            });

            const infoWindow = new google.maps.InfoWindow ({
                content: `<b>${stop.name}</b>`,
            });
            marker. addListener("click", ()=> indoWindow.open (map, marker) );
        });
    }