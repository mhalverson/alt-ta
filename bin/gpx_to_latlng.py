import gpxpy
import sys
filepath = sys.argv[-1]
gpx = gpxpy.parse(open(filepath))
count = 1

def sample(l, one_in=1):
    if one_in == 1:
        return l
    i = 0
    ret_val = [l[i]]
    while i + one_in < len(l):
        i += one_in
        ret_val.append(l[i])
    return ret_val

def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

CHUNK_SIZE = 50
SAMPLING_RATE = 8
DIRECTION = 'forward'
#DIRECTION = 'backward'

if DIRECTION == 'forward':
    ## Normal / forward order
    for track in gpx.tracks:
        for segment in track.segments:
            for chunk in divide_chunks(segment.points, CHUNK_SIZE):
                chunk = sample(chunk, SAMPLING_RATE)
                formatted_points = map(lambda p: '({:.4f},{:.4f})'.format(p.latitude, p.longitude), chunk)
                print('            ' + ', '.join(formatted_points) + ',')
else:
    ## Reverse / backward order
    all_points = []
    for track in gpx.tracks:
        for segment in track.segments:
            all_points.extend(segment.points)
    reversed_points = list(reversed(all_points))
    for chunk in divide_chunks(reversed_points, CHUNK_SIZE):
                chunk = sample(chunk, SAMPLING_RATE)
                formatted_points = map(lambda p: '({:.4f},{:.4f})'.format(p.latitude, p.longitude), chunk)
                print('            ' + ', '.join(formatted_points) + ',')
