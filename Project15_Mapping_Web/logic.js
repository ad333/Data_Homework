// url for past 7 days earthquake data
var earthquakeUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson";

// url for tectonic plates data
// var tectonicUrl = "https://github.com/fraxen/tectonicplates/blob/master/GeoJSON/PB2002_boundaries.json";
var tectonicUrl = "https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_boundaries.json";

// Perform a GET request to the earthquake URL
d3.json(earthquakeUrl, function(edata) {
  // Once we get a response, send the data.features object to the createFeatures function
  createFeatures(edata.features);
});  

function createFeatures(earthquakeData) {

  // Define a function we want to run once for each feature in the features array
  // Give each feature a popup describing the place and time of the earthquake
  function onEachFeature(feature, layer) {
    layer.bindPopup("<h3>" + feature.properties.place +
      "</h3><hr><p>" + new Date(feature.properties.time) + "</p>");
  }

  function pointToLayer(feature, latlng)  {
    return new L.circle(latlng, {
      stroke: false,
      fillOpacity: 0.8,
      fillColor: addColor(feature.properties.mag),
      radius: feature.properties.mag*20000
    })
  }

  function addColor(c)  {
    if (c>5) {return "rgb(255, 0, 0)"}
    else if (c>4) {return "rgb(255, 128, 0)"}
    else if (c>3) {return "rgb(255, 255, 0)"}
    else if (c>2) {return "rgb(153, 153, 0)"}
    else if (c>1) {return "rgb(76, 153, 0)"}
    else {return "rgb(0, 128, 255)"};
  }

  // Create a GeoJSON layer containing the features array on the earthquakeData object
  // Run the onEachFeature and pointToLayer functions once for each piece of data in the array
  var earthquakes = L.geoJSON(earthquakeData, {
    onEachFeature: onEachFeature,
    pointToLayer: pointToLayer
  });

  // Sending our earthquakes layer to the createMap function
  createMap(earthquakes);
}

function createMap(earthquakes) {

  // Define outdoorsmap, darkmap and satellitemap layers
  var outdoorsmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/outdoors-v10/tiles/256/{z}/{x}/{y}?" +
    "access_token=pk.eyJ1IjoiYWQzMzMiLCJhIjoiY2pnd3ZucWszMXVodDMycDlpaWcya3BkdiJ9.mzDXkobnrAckQF1lblrc7w");

  var darkmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/dark-v9/tiles/256/{z}/{x}/{y}?" +
    "access_token=pk.eyJ1IjoiYWQzMzMiLCJhIjoiY2pnd3ZucWszMXVodDMycDlpaWcya3BkdiJ9.mzDXkobnrAckQF1lblrc7w");

    var satellitemap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/satellite-v9/tiles/256/{z}/{x}/{y}?" +
    "access_token=pk.eyJ1IjoiYWQzMzMiLCJhIjoiY2pnd3ZucWszMXVodDMycDlpaWcya3BkdiJ9.mzDXkobnrAckQF1lblrc7w");  

  // Define a baseMaps object to hold our base layers
  var baseMaps = {
    "Outdoors Map": outdoorsmap,
    "Grayscale Map": darkmap,
    "Satellite Map": satellitemap
  };

  var tectonicplates = new L.LayerGroup();
  d3.json(tectonicUrl, function(tData)  {
    L.geoJSON(tData, {}).addTo(tectonicplates);
  });

  // Create overlay object to hold our overlay layer
  var overlayMaps = {
    "Earthquakes": earthquakes,
    "Fault Lines": tectonicplates
  };

  // Create our map, giving it the streetmap and earthquakes layers to display on load
  var myMap = L.map("map", {
    center: [
      37.09, -95.71
    ],
    zoom: 5,
    layers: [outdoorsmap, earthquakes, tectonicplates]
  });

  // Create a layer control
  // Pass in our baseMaps and overlayMaps
  // Add the layer control to the map
  L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
  }).addTo(myMap);
}
