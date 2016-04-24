function populateMap() {
    var appUrl = 'http://ghostgearrecon.us/equipment/list';
//    var data = {equipment: [{latitude: "37.77740", longitude: "-122.40805", retrieved: "false", uuid:"577ba35b-8ff1-42ec-827e-40dcfa3bc2b6", date: "4/15/2016", image:"http://d3ugpfptm7iph0.cloudfront.net/cdn/farfuture/FDMOZScMJHcIbSwO15_7LZFERD8UxD75HnTziOl1umA/mtime:1426523543/sites/default/files/us_files/1014736.jpg"},
//                            {latitude: "37.77740", longitude: "-122.40805", retrieved: "false", uuid:"c995a8a4-5de5-42c8-b57c-eec498be56dc", date: "4/15/2016", image:"http://d3ugpfptm7iph0.cloudfront.net/cdn/farfuture/FDMOZScMJHcIbSwO15_7LZFERD8UxD75HnTziOl1umA/mtime:1426523543/sites/default/files/us_files/1014736.jpg"}
//    ]};
    
    $.get(appUrl, function(data) {
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
            	});
            	if (markers[i].image) {
	            	var feature = marker.feature;
		            // Create custom popup content
		            var popupContent =  '<a target="_blank" class="popup">' +
		                                    '<img src="' + markers[i].image + '" />' +
		                                    '<span>Date: ' + markers[i].date + '</span>' +
		                                '</a>';
		
		            marker.bindPopup(popupContent,{
		                closeButton: false,
		                minWidth: 320
		            });
            	}
            	marker.addTo(map);
            }
        }
    });
        

    $("#changeView").on("click", function() {
		var lat = $('#lat').val(), long = $('#long').val();

		if (lat && long) {
			map.setView([ lat, long ], 9);
		}
	});
}
