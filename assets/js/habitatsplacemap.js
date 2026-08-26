---
layout: none
---

let defaultStyle = {
    color: "#aa002b",
    fillColor: "#aa002b",
    weight: 1,
    opacity: 0.2,
    fillOpacity: 0.2,
}

let hoverStyle = {
    color: "#aa002b",
    fillColor: "#aa002b",
    weight: 3,
    opacity: 0.6,
    fillOpacity: 0.8,
}
let places = {
    {% for post in site.articles %}
    {% if post.path contains "articles/locations/" %}
    "{{post.slug}}" : {
        "label":"{{post.title}}",
        "img":"{{post.coverimg}}",
        "link":"{{post.url}}",
        "description": "{{post.summary}}"
    },
      
    {% endif %}
    {% endfor %}
    

}

loadPlaces()
function loadPlaces(){
    fetch("/assets/geojson/places/southernshores.geojson")
        .then((response) => {
            if (!response.ok) {
                throw new Error(
                    `HTTP error! status: ${response.status}`,
                );
            }
            return response.json(); // Parse incoming string data to JSON object
        })
        .then((geoJsonData) => {
            const geoJsonLayer = L.geoJSON(geoJsonData, {
                
                style: function (feature) {
                    return defaultStyle
                    
                },
                onEachFeature: function (feature, layer) {
                    layer.bindTooltip(feature.properties.name, {
                        sticky: true, // Makes the tooltip follow the mouse
                        direction: 'auto'
                    });

                    if (
                        feature.properties.name
                    ) {
                        let name = feature.properties.name
                        console.log("Clicked on " + name);
                        
                        if(places[name]){
                            const popup = `
                                <div class="habitat-popup">
                                    <img src="${places[name]["img"] || ""}"/>
                                    <h3>${places[name]["label"] || "No Name"}</h3>
                                    <p>${places[name]["description"] || ""}</p>
                                    <a href="${places[name]["link"] || ""}">Read more...</a>
                                </div>
                            `;
                            layer.bindPopup(popup, {
                                maxWidth: 250,
                                className: "habitat-popup-wrapper",
                                closeButton: true,
                            });

                        }
                    }


                    layer.on("mouseover", function (e) {
                        let name = e.target.feature.properties.name
                        console.log(name)
                        geoJsonLayer.eachLayer(function (l) {
                            if (
                                l.feature.properties.name ===
                                name
                            ) {
                                l.setStyle(hoverStyle);
                            }
                        });
                    });

                    // Handle mouseout (Hover Out)
                    layer.on("mouseout", function (e) {
                        let name = e.target.feature.properties.name
                        console.log(name)
                        geoJsonLayer.eachLayer(function (l) {
                            if (
                                l.feature.properties.name ===
                                name
                            ) {
                                l.setStyle(
                                    defaultStyle
                                );
                            }
                        });
                    });

                    layer.on("click", function (e) {
                        
                    });
                },
            });

            geoJsonLayer.bringToFront()
            placeLayers.push(geoJsonLayer)
        })
        .catch((error) => {
            console.error(
                "Error fetching or parsing the GeoJSON file:",
                error,
            );
        });
}