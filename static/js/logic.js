
var countyLayer = []
var heatLayer =[]
var legend2 = L.control({ position: 'bottomright' });
var legend = L.control({ position: 'bottomright' });
function monthlyPayment(p, n, i) {
  return p * i * (Math.pow(1 + i, n)) / (Math.pow(1 + i, n) - 1);
}

//

function createMap(heatArray, geojson) {
  var graymap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "Map data &copy; <a href='https://www.openstreetmap.org/'>OpenStreetMap</a> contributors, <a href='https://creativecommons.org/licenses/by-sa/2.0/'>CC-BY-SA</a>, Imagery © <a href='https://www.mapbox.com/'>Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.light",
    accessToken: API_KEY
  })

  var satmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.satellite",
    accessToken: API_KEY
  })

  //Outdoors Layer
  var outdoors = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/outdoors-v10/tiles/256/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "Map data &copy; <a href='https://www.openstreetmap.org/'>OpenStreetMap</a> contributors, <a href='https://creativecommons.org/licenses/by-sa/2.0/'>CC-BY-SA</a>, Imagery © <a href='https://www.mapbox.com/'>Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.outdoors",
    accessToken: API_KEY
  })


// Creating map object
var myMap = L.map("map", {
  center: [32.1656, -82.9001],
  zoom: 8,
  layers: [graymap, satmap, outdoors]
});
//
var basemaps = {
  "Satellite Map": satmap,
  "Gray Map": graymap,
  "Outdoors": outdoors,
}

var overlay = {
  "Heat Map": heatArray,
  "Fault Lines": geojson,
}
console.log(geojson)
L.control.layers(basemaps, overlay).addTo(myMap)

// This function determines the color of the marker based on the magnitude of the earthquake.
function getColor(magnitude) {
  //console.log(magnitude)
  switch (true) {
    case magnitude > 40:
      return "#FF00FF";
    case magnitude > 30:
      return "#FF0000";
    case magnitude > 20:
      return "#FFFF00";
    case magnitude > 15:
      return "#00FF00";
    case magnitude > 10:
      return "#00FFFF";
    case magnitude > 5:
      return "#0000FF";
    default:
      return "#FFFFFF";
  }
}



legend.onAdd = function () {
  
  var div = L.DomUtil.create('div', 'info legend'),

    grades = [0, 5, 10, 15, 20, 30, 40];

  //Legend Label Earthquake <break> Magnitude  
  div.innerHTML += 'Poverty Rate<br>'

  // loop through our density intervals and generate a label with a colored square for each interval
  for (var i = 0; i < grades.length; i++) {
    div.innerHTML +=
      '<i style="background:' + getColor(grades[i] + 1) + '">&nbsp&nbsp&nbsp&nbsp</i> ' +
      grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
  }

  return div;
};
//Adds Legend to myMap
legend.addTo(myMap);

}
//
// L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
//   attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
//   tileSize: 512,
//   maxZoom: 18,
//   zoomOffset: -1,
//   id: "mapbox/streets-v11",
//   accessToken: API_KEY
// }).addTo(myMap);

// Load in geojson data
//var geoData = "static/data/ny_new_york_zip_codes_geo.min.json";
var geoData = 'static/data/ga_merge.json';

var geojson;

// Grab data with d3
d3.json(geoData, function(data) {
 //console.log(data)
 var countyLines = new L.LayerGroup()
 var heatLines = new L.LayerGroup()
 //
 var heatArray = [];
 var heatdetails =[];
  for (var i = 0; i < data.features.length; i++) {
    var location = data.features[i].properties;

    if (location) {
      var lat = location.INTPTLAT10.replace('+','')
      lat = parseFloat(lat)
      var long = parseFloat(location.INTPTLON10)
      var par = location.Poverty_Rate/location.Population
      var pr = location.Poverty_Rate
      var hi = location.Household_Income
      var hp = location["2021-04-30"]
      var ci = location.City
      var cn = location.CountyName
      var mx = (hi/12)*0.28
      var intrest = 3.25/100/12
      var mp = monthlyPayment(hp, 360, intrest )
      var ob = 100*(mp/mx)
      //console.log(mp)
      heatArray.push([lat, long, par]);
      heatdetails.push([lat, long, pr, hi, hp, ci, cn, mx, mp,ob ])
    }
    
  }
  //console.log(heatArray)
  var heat = L.heatLayer(heatArray, {
    radius: 35,
    opacity: 1,
    gradient: {
              0.01: "rgb(255,255,255)",
              0.05: "rgb(0,0,255)",
              0.10: "rgb(0,255,255)",
              0.15: "rgb(0,255,0)",
              0.20: "rgb(255,255,0)",
              0.30:  "rgb(255,0,0)",
              0.40: "rgb(255,0,255)"                     }
    
  }).addTo(heatLines)
  //
  var index = 0;
    var id = setInterval(function(){
        heat.addLatLng(heatArray[index++]);
        if(index >= heatArray.length - 1){ clearInterval(id); }
    }, 200);

    
    // add markers
    heatdetails.forEach(function(d){
        //console.log(heatdetails)
        var popup = L.popup().setContent("Poverty Rate : " + d[2].toFixed(0)+ "% " + "<br> Household Income : $" +d[3]+"<br>Median single family home price: $" + d[4]+"<br>Mortgage (28% rule) : $"+ d[7].toFixed(0) + "<br>Monthly mortgage payment base on your area : $"+d[8].toFixed(0)+"<br>Monthly income overspend on housing : "+d[9].toFixed(2)+"% " +"<br>City : " +d[5]+"<br>County : " + d[6]);
        L.marker([d[0],d[1]], {opacity: 0}) // hide points
          .bindPopup(popup,{keepInView: true}).openPopup()
          .addTo(heatLines);
    });

  //

  // Create a new choropleth layer
  geojson = L.choropleth(data, {

    // Define what  property in the features to use
    valueProperty: "2021-04-30",

    // Set color scale
    scale: ["#ffffb2", "#b10026"],

    // Number of breaks in step range
    steps: 10,

    // q for quartile, e for equidistant, k for k-means
    mode: "q",
    style: {
      // Border color
      color: "#fff",
      weight: 1,
      fillOpacity: 0.8
    },

    // Binding a pop-up to each layer
    onEachFeature: function(feature, layer) {
      
      layer.bindPopup("Zip Code: " + feature.properties.ZCTA5CE10 + "<br>Median single family home price: $" + feature.properties["2021-04-30"]+ "<br>City : " + feature.properties.City + "<br>County : " +feature.properties.CountyName + "<br> Household Income : $" + feature.properties.Household_Income + "<br> Poverty Rate: " + feature.properties.Poverty_Rate.toFixed(0) +"%");
    }
    
  }).addTo(countyLines);
  //
  countyLayer = countyLines
  heatLayer = heatLines
  createMap(heatLayer, countyLayer)

  
  // Set up the legend
  
  legend2.onAdd = function() {
    var div = L.DomUtil.create("div", "info legend");
    var limits = geojson.options.limits;
    var colors = geojson.options.colors;
    var labels = [];

    // Add min & max
    var legendInfo = "<h1>Median Home Price</h1>" +
      "<div class=\"labels\">" +
        "<div class=\"min\"> $" + limits[0] + "</div>" +
        "<div class=\"max\"> $" + limits[limits.length - 1] + "</div>" +
      "</div>";

    div.innerHTML = legendInfo;

    limits.forEach(function(limit, index) {
      labels.push("<li style=\"background-color: " + colors[index] + "\">$ "+limit.toFixed(2)+"</li>");
    });

    div.innerHTML += "<ul>" + labels.join("") + "</ul>";
    return div;
  };
  
  // Adding legend to the map
  legend2.addTo(myMap);

});
