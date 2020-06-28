import os

import folium
import gpxpy

from route import (
    KEY_SHORT_DESC,
    KEY_LOCATION,
    KEY_WAYPOINTS,
    KEY_NOTES,
    KEY_LINKS,
    linkify,
    proposed_route,
    alternate_routes,
)

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
HTML_DIR = os.path.join(BASE_DIR, 'html')

# Create the base map with tilesets
MAP_DEFAULT_LOCATION = (-45.3010,167.4283)

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

for route in proposed_route:
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
