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
    {   KEY_WAYPOINTS: ((-40.7819, 172.9978), (-40.8043, 173.0060), (-40.8165, 172.9772), (-40.8328, 172.9683),),
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
