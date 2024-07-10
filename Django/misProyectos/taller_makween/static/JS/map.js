document.addEventListener("DOMContentLoaded", function() {
    var MapAPI = {
        initMap: function(mapId, center, zoom) {
            var map = L.map(mapId).setView(center, zoom);
            console.log('ID mapa:', mapId, 'Center:', center, 'Zoom:', zoom);
            return map;
        },

        addTileLayer: function(map, tileUrl, attribution) {
            var tileLayer = L.tileLayer(tileUrl, {
                attribution: attribution
            }).addTo(map);
            console.log('Layers agregados al mapa:', tileUrl, 'Atributos:', attribution);
            return tileLayer;
        },

        addMarker: function(map, latlng, popupContent) {
            var marker = L.marker(latlng).addTo(map);
            if (popupContent) {
                marker.bindPopup(popupContent).openPopup();
            }
            console.log('Coordenadas del mapa:', latlng, 'Contenido del popup:', popupContent);
            return marker;
        }
    };

    var map = MapAPI.initMap('map', [-33.02430131558989, -71.55260496332097], 14);

    MapAPI.addTileLayer(map, 'https://tile.openstreetmap.org/{z}/{x}/{y}.png', '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors');

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    L.marker([-33.02430131558989, -71.55260496332097]).addTo(map)
        .bindPopup('TallerMqueen')
        .openPopup();
});
