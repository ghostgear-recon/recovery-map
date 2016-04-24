function populateMap() {
    var appUrl = 'http://ghostgearrecon.us/equipment/list';
    var data = {equipment: [{latitude: "37.77740", longitude: "-122.40805", retrieved: "false", uuid:"577ba35b-8ff1-42ec-827e-40dcfa3bc2b6"},
                            {latitude: "37.77740", longitude: "-122.40805", retrieved: "false", uuid:"c995a8a4-5de5-42c8-b57c-eec498be56dc"}
    ]};
    
    //$.get(appUrl, function(data) {
        console.log(data);
        L.mapbox.accessToken = 'pk.eyJ1IjoiZWNvYW5kcmV3dHJjIiwiYSI6InZ0MzhibUkifQ.Q0qYLMThqHqmAJ3q3dxvog';
        var map = L.mapbox.map('map', 'mapbox.streets').setView([37.5871329,-121.9321825], 9);
        if (data) {
        	var marker;
        	var markers = data.equipment;
            for (var i = 0; i < markers.length; i++) {
            	marker = L.marker([markers[i].latitude, markers[i].longitude], {
            	    icon: L.mapbox.marker.icon({
            	      'marker-color': '#f86767'
            	    }),
            	    draggable: true
            	}).addTo(map);
            }
        }
    //});
        

    $("#changeView").on("click", function() {
		var lat = $('#lat').val(), long = $('#long').val();

		if (lat && long) {
			map.setView([ lat, long ], 9);
		}
	});
}
