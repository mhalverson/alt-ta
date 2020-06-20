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
    name='NZ Topo50',
    tiles='http://tiles-{s}.data-cdn.linz.govt.nz/services;key=' + LINZ_API_KEY + '/tiles/v4/layer=50767/EPSG:3857/{z}/{x}/{y}.png',
    attr='<a href=“http://data.linz.govt.nz”>Sourced from LINZ. CC BY 4.0</a>',
    subdomains='abcd',
)
topo.add_to(m)

m.add_child(folium.LatLngPopup()) # enable this if you want to click to see the LatLng

# routes / campsites

KEY_SHORT_DESC = 'short_desc'
KEY_LOCATION = 'location'
KEY_WAYPOINTS = 'waypoints'

route = [
    { KEY_SHORT_DESC: 'Road end', KEY_LOCATION: (-40.8098, 172.9563), },
    { KEY_SHORT_DESC: 'Whariwharangi Hut', KEY_LOCATION: (-40.7890, 172.9744), },
    { KEY_SHORT_DESC: 'Separation Point', KEY_LOCATION: latlng_separation_point, },
    { KEY_WAYPOINTS: ((-40.8043, 173.0060), (-40.8165, 172.9772), (-40.8328, 172.9683),),
      KEY_SHORT_DESC: 'Awapoto Hut', KEY_LOCATION: (-40.8627, 172.9388), },
    { KEY_SHORT_DESC: 'Wainui Hut', KEY_LOCATION: (-40.9147, 172.9203), },
    { KEY_WAYPOINTS: ((-40.9377, 172.9003), (-40.8970, 172.7300),),
      KEY_SHORT_DESC: 'Anatoki Forks Hut', KEY_LOCATION: (-40.9396, 172.6084), },
    { KEY_SHORT_DESC: 'Adelaide Tarn', KEY_LOCATION: (-40.9430, 172.5435), },
    { KEY_SHORT_DESC: 'Lonely Lake', KEY_LOCATION: (-40.9828, 172.5580), },
    { KEY_WAYPOINTS: ((-41.0357, 172.5494),),
      KEY_SHORT_DESC: 'Fenella', KEY_LOCATION: (-41.04960, 172.52520), },
]

# put it all together

# Camp
fg_camp_name = 'Campsites'
fg_camp = folium.FeatureGroup(name=fg_camp_name, show=True)
fg_camp.add_to(m)

for x in route:
    popup = folium.Popup(x[KEY_SHORT_DESC])
    marker = folium.Marker(
        location=x[KEY_LOCATION],
        popup=popup,
    )
    marker.add_to(fg_camp)

# Route
fg_route = folium.FeatureGroup(name='Route', show=True)
fg_route.add_to(m)

for i, day in enumerate(route):
    leg = []
    if i == 0:
        pass # do nothing!
    else:
        wake_up_coord = route[i-1][KEY_LOCATION]
        leg.append(wake_up_coord)
    if day.get(KEY_WAYPOINTS):
        leg.extend(day[KEY_WAYPOINTS])
    sleep_coord = day[KEY_LOCATION]
    leg.append(sleep_coord)

    if len(leg) < 2:
        continue

    folium.PolyLine(
        locations=leg,
        color='#FF0000',
        weight=5,
        #popup='{}'.format(day[DAY_DATE]),
    ).add_to(fg_route)

# LayerControl - this has to come after all the FeatureGroups
folium.LayerControl().add_to(m)

# Write to file and call it a day
map_filename = os.path.join(HTML_DIR, 'map.html')
print('Writing map HTML to file: {}'.format(map_filename))
with open(map_filename, 'w'):
    m.save(map_filename)
