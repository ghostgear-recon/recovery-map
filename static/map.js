function populateMap() {
    var appUrl = 'http://ghostgearrecon.us/equipment/list';
    var data = {};
    $.get(appUrl, function(data) {
        console.log(data);
        L.mapbox.accessToken = 'pk.eyJ1IjoiZWNvYW5kcmV3dHJjIiwiYSI6InZ0MzhibUkifQ.Q0qYLMThqHqmAJ3q3dxvog';
        var map = L.mapbox.map('map', 'mapbox.streets');
    });
}
