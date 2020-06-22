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
KEY_LINKS = 'links'

point_adelaide_tarn = (-40.9430, 172.5435)
desc_adelaide_tarn = 'Adelaide Tarn Hut'
point_trevor_carter = (-41.3983, 172.3886)

def linkify(url, label):
    return '<a href="' + url + '" target="_blank">' + label + '</a>'

route = [
    {   KEY_SHORT_DESC: 'Road end',
        KEY_LOCATION: (-40.8098, 172.9563), },
    {   KEY_NOTES: '6 km',
        KEY_LINKS: [['DOC Whariwharangi Hut', 'https://www.doc.govt.nz/parks-and-recreation/places-to-go/nelson-tasman/places/abel-tasman-national-park/things-to-do/huts/whariwharangi-hut/']],
        KEY_SHORT_DESC: 'Whariwharangi Hut',
        KEY_LOCATION: (-40.7890, 172.9744), },
    {   KEY_WAYPOINTS: (latlng_separation_point, (-40.8043, 173.0060), (-40.8165, 172.9772), (-40.8328, 172.9683),),
        KEY_NOTES: '21 km ish',
        KEY_LINKS: [
            ['DOC Awapoto Hut', 'https://www.doc.govt.nz/parks-and-recreation/places-to-go/nelson-tasman/places/abel-tasman-national-park/things-to-do/huts/awapoto-hut/'],
            ['WildThings Separation Point Loop', 'https://www.wildthings.club/trails/tasman/takaka/separation-point-loop/'],
        ],
        KEY_SHORT_DESC: 'Awapoto Hut',
        KEY_LOCATION: (-40.8627, 172.9388), },
    {   KEY_WAYPOINTS: ((-40.8983, 172.9252), (-40.9144, 172.9357), (-40.9331, 172.9286)),
        KEY_NOTES: '17 km',
        KEY_LINKS: [['DOC Canaan Downs campsite', 'https://www.doc.govt.nz/parks-and-recreation/places-to-go/nelson-tasman/places/canaan-downs-scenic-reserve/things-to-do/campsites/canaan-downs-campsite/']],
        KEY_SHORT_DESC: 'Canaan Downs Campsite',
        KEY_LOCATION: (-40.9420, 172.8918), },
    {   KEY_WAYPOINTS: ((-40.9377, 172.9003), (-40.9163, 172.8591), (-40.8928, 172.8409),),
        KEY_NOTES: '10 km + road, Rameka is MTB track, Harwoods Hole detour?',
        KEY_SHORT_DESC: 'Takaka',
        KEY_LOCATION: (-40.8524, 172.8053), },
    {   KEY_WAYPOINTS: ((-40.8719, 172.8059), (-40.9079, 172.7648), (-40.8968, 172.7465), (-40.8970, 172.7300), (-40.9011, 172.7256), (-40.8994, 172.7124), (-40.9230, 172.6869), (-40.9320, 172.6213)),
        KEY_NOTES: '18 km track (8 hrs) + road',
        KEY_LINKS: [['DOC Anatoki Track', 'https://www.doc.govt.nz/parks-and-recreation/places-to-go/nelson-tasman/places/kahurangi-national-park/things-to-do/tracks/anatoki-and-historic-kill-devil-pack-tracks/']],
        KEY_SHORT_DESC: 'Anatoki Forks Hut',
        KEY_LOCATION: (-40.9396, 172.6084), },
    {   KEY_WAYPOINTS: (),
        KEY_NOTES: '5-6 hrs',
        KEY_LINKS: [['DOC Douglas Range guide', 'https://www.doc.govt.nz/globalassets/documents/parks-and-recreation/tracks-and-walks/nelson-marlborough/douglas-range-guide.pdf']],
        KEY_SHORT_DESC: desc_adelaide_tarn,
        KEY_LOCATION: point_adelaide_tarn, },
    {   KEY_WAYPOINTS: ((-40.9635, 172.5722), (-40.9741, 172.5652), (-40.9748, 172.5532)),
        KEY_NOTES: '8-10 hrs',
        KEY_LINKS: [
            ['DOC Douglas Range guide', 'https://www.doc.govt.nz/globalassets/documents/parks-and-recreation/tracks-and-walks/nelson-marlborough/douglas-range-guide.pdf'],
            ['tramping.net Dragons Teeth', 'https://tramping.net.nz/routes/dragons-teeth-route-kahurangi-national-park'],
        ],
        KEY_SHORT_DESC: 'Lonely Lake Hut',
        KEY_LOCATION: (-40.9828, 172.5580), },
    {   KEY_WAYPOINTS: ((-41.0357, 172.5494),),
        KEY_NOTES: '6-8 hrs',
        KEY_LINKS: [
            ['DOC Douglas Range guide', 'https://www.doc.govt.nz/globalassets/documents/parks-and-recreation/tracks-and-walks/nelson-marlborough/douglas-range-guide.pdf'],
            ['tramping.net Dragons Teeth', 'https://tramping.net.nz/routes/dragons-teeth-route-kahurangi-national-park'],
        ],
        KEY_SHORT_DESC: 'Fenella Hut',
        KEY_LOCATION: (-41.04960, 172.52520), },
    {   KEY_NOTES: '4-5 hrs',
        KEY_LINKS: [
            ['DOC Douglas Range guide', 'https://www.doc.govt.nz/globalassets/documents/parks-and-recreation/tracks-and-walks/nelson-marlborough/douglas-range-guide.pdf'],
            ['tramping.net Dragons Teeth', 'https://tramping.net.nz/routes/dragons-teeth-route-kahurangi-national-park'],
        ],
        KEY_SHORT_DESC: 'Trilobite Hut',
        KEY_LOCATION: (-41.1305, 172.6094), },
    {   KEY_WAYPOINTS: ((-41.1407, 172.6252), (-41.1474, 172.6044), (-41.1853, 172.6296), (-41.2153, 172.5904)),
        KEY_NOTES: '10 hrs (4 to Balloon, 6 thereafter)',
        KEY_LINKS: [
            ['NelsonTrails Balloon Hut', 'https://nelsontrails.co.nz/balloon-hut/'],
            ['DOC Leslie-Karamea', 'https://www.doc.govt.nz/parks-and-recreation/places-to-go/nelson-tasman/places/kahurangi-national-park/things-to-do/tracks/leslie-karamea-track/'],
        ],
        KEY_SHORT_DESC: 'Karamea Bend Hut',
        KEY_LOCATION: (-41.2329, 172.5109), },
    {   KEY_WAYPOINTS: ((-41.2933, 172.4685),),
        KEY_NOTES: '7.5 hrs',
        KEY_LINKS: [['DOC Leslie-Karamea', 'https://www.doc.govt.nz/parks-and-recreation/places-to-go/nelson-tasman/places/kahurangi-national-park/things-to-do/tracks/leslie-karamea-track/']],
        KEY_SHORT_DESC: 'Thor Hut',
        KEY_LOCATION: (-41.3528, 172.4383), },
    {   KEY_WAYPOINTS: ((-41.3842, 172.4189), point_trevor_carter),
        KEY_NOTES: '3.5 hrs + 5 hrs (over the top *or* around)',
        KEY_LINKS: [
            ['DOC Leslie-Karamea', 'https://www.doc.govt.nz/parks-and-recreation/places-to-go/nelson-tasman/places/kahurangi-national-park/things-to-do/tracks/leslie-karamea-track/'],
            ['tramping.net Wangapeka Saddle campsite', 'https://tramping.net.nz/huts-kahurangi/wangapeka-saddle-campsite-kahurangi-national-park'],
            ['DOC Wangapeka Track', 'https://www.doc.govt.nz/parks-and-recreation/places-to-go/nelson-tasman/places/kahurangi-national-park/things-to-do/tracks/wangapeka-track/'],
        ],
        KEY_SHORT_DESC: 'Wangapeka Saddle',
        KEY_LOCATION: (-41.4247, 172.4214), },
    {   KEY_WAYPOINTS: ((-41.4265, 172.4278), (-41.4538, 172.4242), (-41.4799, 172.3945), (-41.5032, 172.4002)),
        KEY_NOTES: '12 hrs',
        KEY_LINKS: [
            ['tramping.net Matiri tops', 'https://tramping.net.nz/routes/matiri-ridge-route-kahurangi-national-park'],
            ['DOC Matiri tops', 'https://www.doc.govt.nz/parks-and-recreation/places-to-go/nelson-tasman/places/kahurangi-national-park/things-to-do/tracks/matiri-valley-and-1000-acre-plateau-tramping-tracks/'],
        ],
        KEY_SHORT_DESC: 'Hurricane Hut',
        KEY_LOCATION: (-41.5068, 172.3822), },
    {   KEY_WAYPOINTS: (),
        KEY_NOTES: '6-7 hrs',
        KEY_LINKS: [['DOC Matiri Valley', 'https://www.doc.govt.nz/parks-and-recreation/places-to-go/nelson-tasman/places/kahurangi-national-park/things-to-do/tracks/matiri-valley-and-1000-acre-plateau-tramping-tracks']],
        KEY_SHORT_DESC: 'McConchies Hut',
        KEY_LOCATION: (-41.5872, 172.3631), },
    {   KEY_WAYPOINTS: ((-41.6565, 172.3291),),
        KEY_NOTES: '8 hrs',
        KEY_LINKS: [['DOC Matiri Valley', 'https://www.doc.govt.nz/parks-and-recreation/places-to-go/nelson-tasman/places/kahurangi-national-park/things-to-do/tracks/matiri-valley-and-1000-acre-plateau-tramping-tracks']],
        KEY_SHORT_DESC: 'Matiri road-end',
        KEY_LOCATION: (-41.7053, 172.3302), },
    {   KEY_SHORT_DESC: 'Murchison',
        KEY_NOTES: 'walk, bike, or hitch?',
        KEY_LOCATION: (-41.8069, 172.3247), },
]

alternate_routes = [
  [
    # Farewell Spit to Adelaide
    { KEY_SHORT_DESC: 'Farewell Spit', KEY_LOCATION: (-40.5107, 172.7465), },
    { KEY_WAYPOINTS: ((-40.5003, 172.6853), (-40.5146, 172.6471), (-40.5302, 172.6376), (-40.5540, 172.6308), (-40.5842, 172.6325), (-40.5965, 172.5803), (-40.6154, 172.5510), (-40.6397, 172.5596), (-40.6962, 172.5409), (-40.7194, 172.5806), (-40.7797, 172.5591), (-40.8227, 172.5791), (-40.8425, 172.5581), (-40.8798, 172.5832), (-40.9003, 172.5793), (-40.9191, 172.5534), (-40.9334, 172.5553), (-40.9393, 172.5498), (-40.9430, 172.5517)),
      KEY_LINKS: [['WildThings Boulder Lake to Adelaide Tarn', 'https://www.wildthings.club/trails/tasman/takaka/boulder-lake-to-anatoki-forks/?']],
      KEY_SHORT_DESC: desc_adelaide_tarn, KEY_LOCATION: point_adelaide_tarn, },
  ],
  [
    # Wangapeka to OGR
    { KEY_SHORT_DESC: 'Trevor Carter Hut', KEY_LOCATION: point_trevor_carter, },
    { KEY_WAYPOINTS: ((-41.3888, 172.3652), (-41.3972, 172.2952), (-41.3697, 172.2666), (-41.4229, 172.2426), (-41.4670, 172.2770), (-41.4664, 172.2388), (-41.4957, 172.2340), (-41.5147, 172.1969), (-41.5481, 172.1787), (-41.6056, 172.1994), (-41.6865, 172.2025), (-41.7234, 172.0984)),
      KEY_LINKS: [['RemoteHuts Johnson Hut', 'http://remotehuts.co.nz/huts/Johnson_Hut/']],
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

    popup_text = [
        'Day ' + str(i) + ':',
        day.get(KEY_NOTES) or '',
    ]
    for j, link in enumerate(day.get(KEY_LINKS, [])):
        popup_text.append(linkify(link[1], link[0]))
    folium.PolyLine(
        locations=leg,
        color='#ce4429',
        weight=5,
        popup=folium.Popup(html='<br/>'.join(popup_text), max_width=300),
    ).add_to(fg_proposed)

# Layer - Alternate routes
fg_alternate = folium.FeatureGroup(name='Alternate routes', show=True)
fg_alternate.add_to(m)

for route in alternate_routes:
    for i, day in enumerate(route):
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

        popup_text = day.get(KEY_NOTES) or []
        for j, link in enumerate(day.get(KEY_LINKS, [])):
            popup_text.append(linkify(link[1], link[0]))
        folium.PolyLine(
            locations=leg,
            color='#8486d3',
            weight=5,
            popup=folium.Popup(html='<br/>'.join(popup_text), max_width=300),
        ).add_to(fg_alternate)

# LayerControl - this has to come after all the FeatureGroups
folium.LayerControl(collapsed=False).add_to(m)

# Write to file and call it a day
map_filename = os.path.join(HTML_DIR, 'map.html')
print('Writing map HTML to file: {}'.format(map_filename))
with open(map_filename, 'w'):
    m.save(map_filename)
