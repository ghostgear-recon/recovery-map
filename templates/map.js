function populateMap() {
	var appUrl = 'http://ghostgearrecon.us/equipment/list';
    var data = {};
	$.get(url, function(data) {
			console.log(data);
			L.mapbox.accessToken = '<your access token here>';
			var map = L.mapbox.map('map', 'mapbox.k8xv42t9').setView([38.909671288923, -77.034084142948], 13).featureLayer.setGeoJSON(data);
		}
	});
}



