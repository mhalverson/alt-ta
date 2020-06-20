import os

import folium

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
HTML_DIR = os.path.join(BASE_DIR, 'html')

# map
latlng_separation_point = (-40.7819, 172.9978)
MAP_DEFAULT_LOCATION = latlng_separation_point

m = folium.Map(
    location=MAP_DEFAULT_LOCATION,
    zoom_start=12,
    control_scale=True, # show a scale bar e.g. "100 km" or "50 mi"
    tiles=None,
)

LINZ_API_KEY_PATH = os.path.join(BASE_DIR, 'LINZ_API_KEY')
LINZ_API_KEY = open(LINZ_API_KEY_PATH).readlines()[0].strip()
if not LINZ_API_KEY:
    raise ValueError('no LINZ_API_KEY found at {}'.format(LINZ_API_KEY_PATH))

topo = folium.TileLayer(
    name='NZ Topo 50',
    tiles='http://tiles-{s}.data-cdn.linz.govt.nz/services;key=' + LINZ_API_KEY + '/tiles/v4/layer=50767/EPSG:3857/{z}/{x}/{y}.png',
    attr='<a href=“http://data.linz.govt.nz”>Sourced from LINZ. CC BY 4.0</a>',
    subdomains='abcd',
)
topo.add_to(m)

m.add_child(folium.LatLngPopup()) # enable this if you want to click to see the LatLng

# routes / campsites

KEY_SHORT_DESC = 'short_desc'
KEY_LOCATION = 'location'

campsites = [
    {
        KEY_SHORT_DESC: 'Separation Point',
        KEY_LOCATION: latlng_separation_point,
    },
    {
        KEY_SHORT_DESC: 'Awapoto Hut',
        KEY_LOCATION: (-40.8627, 172.9388),
    },
]

# put it all together

for x in campsites:
    popup = folium.Popup(x[KEY_SHORT_DESC])
    marker = folium.Marker(
        location=x[KEY_LOCATION],
        popup=popup,
    )
    marker.add_to(m)


map_filename = os.path.join(HTML_DIR, 'map.html')
print('Writing map HTML to file: {}'.format(map_filename))
with open(map_filename, 'w'):
    m.save(map_filename)
