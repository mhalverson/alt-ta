import os

import folium
import gpxpy

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
HTML_DIR = os.path.join(BASE_DIR, 'html')

# Create the base map with tilesets
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


topos = [['NZ Topo50', '50767'],
         ['NZ Topo250', '50798']] # TODO when zooming, the tile layer should automatically switch between Topo50 and Topo250
for topo in topos:
    topo_layer = folium.TileLayer(
        name=topo[0],
        tiles='http://tiles-{s}.data-cdn.linz.govt.nz/services;key=' + LINZ_API_KEY + '/tiles/v4/layer=' + topo[1] + '/EPSG:3857/{z}/{x}/{y}.png',
        attr='<a href="http://data.linz.govt.nz">Sourced from LINZ. CC BY 4.0</a>',
        subdomains='abcd',
    )
    topo_layer.add_to(m)

m.add_child(folium.LatLngPopup()) # enable this if you want to click to see the LatLng

# Data for the actual proposed route (and alternate routes)
KEY_SHORT_DESC = 'short_desc'
KEY_LOCATION = 'location'
KEY_WAYPOINTS = 'waypoints'
KEY_NOTES = 'notes'

point_adelaide_tarn = (-40.9430, 172.5435)
desc_adelaide_tarn = 'Adelaide Tarn'
point_trevor_carter = (-41.3983, 172.3886)

route = [
    { KEY_SHORT_DESC: 'Road end', KEY_LOCATION: (-40.8098, 172.9563), },
    { KEY_SHORT_DESC: 'Whariwharangi Hut', KEY_LOCATION: (-40.7890, 172.9744), },
    { KEY_SHORT_DESC: 'Separation Point', KEY_LOCATION: latlng_separation_point, },
    { KEY_WAYPOINTS: ((-40.8043, 173.0060), (-40.8165, 172.9772), (-40.8328, 172.9683),),
      KEY_SHORT_DESC: 'Awapoto Hut', KEY_LOCATION: (-40.8627, 172.9388), },
    { KEY_SHORT_DESC: 'Wainui Hut', KEY_LOCATION: (-40.9147, 172.9203), },
    { KEY_WAYPOINTS: ((-40.9377, 172.9003), (-40.8970, 172.7300),),
      KEY_SHORT_DESC: 'Anatoki Forks Hut', KEY_LOCATION: (-40.9396, 172.6084), },
    { KEY_SHORT_DESC: desc_adelaide_tarn, KEY_LOCATION: point_adelaide_tarn, },
    { KEY_SHORT_DESC: 'Lonely Lake', KEY_LOCATION: (-40.9828, 172.5580), },
    { KEY_WAYPOINTS: ((-41.0357, 172.5494),),
      KEY_SHORT_DESC: 'Fenella', KEY_LOCATION: (-41.04960, 172.52520), },
    { KEY_SHORT_DESC: 'Trilobite', KEY_LOCATION: (-41.1305, 172.6094), },
    { KEY_WAYPOINTS: ((-41.1407, 172.6252), (-41.1474, 172.6044), (-41.1853, 172.6296), (-41.2153, 172.5904)),
      KEY_SHORT_DESC: 'Karamea Bend', KEY_LOCATION: (-41.2329, 172.5109), },
    { KEY_WAYPOINTS: ((-41.2933, 172.4685), (-41.3842, 172.4189), point_trevor_carter),
      KEY_SHORT_DESC: 'Stone', KEY_LOCATION: (-41.4208, 172.4392), },
    { KEY_WAYPOINTS: ((-41.4265, 172.4278), (-41.4538, 172.4242), (-41.4799, 172.3945), (-41.5032, 172.4002)),
      KEY_NOTES: 'Stone to Hurricane - see <a href="https://www.doc.govt.nz/parks-and-recreation/places-to-go/nelson-tasman/places/kahurangi-national-park/things-to-do/tracks/matiri-valley-and-1000-acre-plateau-tramping-tracks/">link</a>',
      KEY_SHORT_DESC: 'Hurricane', KEY_LOCATION: (-41.5068, 172.3822), },
    { KEY_WAYPOINTS: ((-41.5872, 172.3631),),
      KEY_SHORT_DESC: 'Lake Matiri', KEY_LOCATION: (-41.6565, 172.3291), },
    { KEY_SHORT_DESC: 'Murchison', KEY_LOCATION: (-41.8069, 172.3247), },
]

alternate_routes = [
  [
    # Farewell Spit to Adelaide
    { KEY_SHORT_DESC: 'Farewell Spit', KEY_LOCATION: (-40.5107, 172.7465), },
    { KEY_WAYPOINTS: ((-40.5003, 172.6853), (-40.5146, 172.6471), (-40.5302, 172.6376), (-40.5540, 172.6308), (-40.5842, 172.6325), (-40.5965, 172.5803), (-40.6154, 172.5510), (-40.6397, 172.5596), (-40.6962, 172.5409), (-40.7194, 172.5806), (-40.7797, 172.5591), (-40.8227, 172.5791), (-40.8425, 172.5581), (-40.8798, 172.5832), (-40.9003, 172.5793), (-40.9191, 172.5534), (-40.9334, 172.5553), (-40.9393, 172.5498), (-40.9430, 172.5517)),
      KEY_NOTES: 'Boulder Lake to Adelaide - <a href="https://www.wildthings.club/trails/tasman/takaka/boulder-lake-to-anatoki-forks/?">link</a>',
      KEY_SHORT_DESC: desc_adelaide_tarn, KEY_LOCATION: point_adelaide_tarn, },
  ],
  [
    # Wangapeka to OGR
    { KEY_SHORT_DESC: 'Trevor Carter Hut', KEY_LOCATION: point_trevor_carter, },
    { KEY_WAYPOINTS: ((-41.3888, 172.3652), (-41.3972, 172.2952), (-41.3697, 172.2666), (-41.4229, 172.2426), (-41.4670, 172.2770), (-41.4664, 172.2388), (-41.4957, 172.2340), (-41.5147, 172.1969), (-41.5481, 172.1787), (-41.6056, 172.1994), (-41.6865, 172.2025), (-41.7234, 172.0984)),
      KEY_NOTES: 'Johnson Hut to OGR - <a href="http://remotehuts.co.nz/huts/Johnson_Hut/">link</a>',
      KEY_SHORT_DESC: 'Old Ghost Road - Lyell', KEY_LOCATION: (-41.7959, 172.0497), },
  ],
]

# Layer - The actual Te Araroa
TA_GPX_PATH = os.path.join(BASE_DIR, 'TeAraroaTrail_asRoute.gpx') # courtesy of https://www.teararoa.org.nz/downloads/ - manually edited to remove the North Island routes
gpx = gpxpy.parse(open(TA_GPX_PATH))
fg_actual_ta = folium.FeatureGroup(name='The actual Te Araroa', show=True)
fg_actual_ta.add_to(m)

for r in gpx.routes:
    leg_start = r.points[0]
    folium.Marker(location=(leg_start.latitude, leg_start.longitude)).add_to(fg_actual_ta)
    leg = []
    for p in r.points:
        leg.append((p.latitude, p.longitude))
    folium.PolyLine(
        locations=leg,
        color='#5fbb4f', # recommendations at https://www.linz.govt.nz/data/linz-data-service/guides-and-documentation/styling-hints-and-tips-for-linz-basemaps
        weight=5,
        popup=r.name,
    ).add_to(fg_actual_ta)
very_end = gpx.routes[-1].points[-1]
folium.Marker(location=(very_end.latitude, very_end.longitude)).add_to(fg_actual_ta)

# Layer - notes
fg_notes = folium.FeatureGroup(name='Notes', show=False)
fg_notes.add_to(m)

# Layer - Proposed route
fg_proposed = folium.FeatureGroup(name='Proposed route', show=True)
fg_proposed.add_to(m)

for i, day in enumerate(route):
    popup = folium.Popup(day[KEY_SHORT_DESC])
    marker = folium.Marker(
        location=day[KEY_LOCATION],
        popup=popup,
    )
    marker.add_to(fg_proposed)

    leg = []
    if i == 0:
        pass # do nothing!
    else:
        yesterday = route[i-1]
        wake_up_coord = yesterday[KEY_LOCATION]
        leg.append(wake_up_coord)
    if day.get(KEY_WAYPOINTS):
        leg.extend(day[KEY_WAYPOINTS])
    sleep_coord = day[KEY_LOCATION]
    leg.append(sleep_coord)

    if len(leg) < 2:
        continue

    folium.PolyLine(
        locations=leg,
        color='#ce4429',
        weight=5,
    ).add_to(fg_proposed)
    if day.get(KEY_NOTES):
        folium.PolyLine(
            locations=leg,
            color='#ff69b4',
            weight=10,
            popup=folium.Popup(html=day[KEY_NOTES]),
        ).add_to(fg_notes)

# Layer - Alternate routes
fg_alternate = folium.FeatureGroup(name='Alternate routes', show=True)
fg_alternate.add_to(m)

for route in alternate_routes:
    for i, day in enumerate(route):
        popup = folium.Popup(day[KEY_SHORT_DESC])
        marker = folium.Marker(
            location=day[KEY_LOCATION],
            popup=popup,
        )
        marker.add_to(fg_alternate)

        leg = []
        if i == 0:
            pass # do nothing!
        else:
            yesterday = route[i-1]
            wake_up_coord = yesterday[KEY_LOCATION]
            leg.append(wake_up_coord)
        if day.get(KEY_WAYPOINTS):
            leg.extend(day[KEY_WAYPOINTS])
        sleep_coord = day[KEY_LOCATION]
        leg.append(sleep_coord)

        if len(leg) < 2:
            continue

        folium.PolyLine(
            locations=leg,
            color='#8486d3',
            weight=5,
        ).add_to(fg_alternate)
        if day.get(KEY_NOTES):
            folium.PolyLine(
                locations=leg,
                color='#ff69b4',
                weight=10,
                popup=folium.Popup(html=day[KEY_NOTES]),
            ).add_to(fg_notes)

# LayerControl - this has to come after all the FeatureGroups
folium.LayerControl(collapsed=False).add_to(m)

# Write to file and call it a day
map_filename = os.path.join(HTML_DIR, 'map.html')
print('Writing map HTML to file: {}'.format(map_filename))
with open(map_filename, 'w'):
    m.save(map_filename)
