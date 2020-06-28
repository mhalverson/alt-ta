#!/usr/local/bin/python3
import gpxpy
import sys
filepath = sys.argv[-1]
gpx = gpxpy.parse(open(filepath))
count = 1

def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

## Normal / forward order
#for track in gpx.tracks:
#    for segment in track.segments:
#        for chunk in divide_chunks(segment.points, 10):
#            formatted_points = map(lambda p: '({:.4f},{:.4f})'.format(p.latitude, p.longitude), chunk)
#            print('            ' + ', '.join(formatted_points) + ',')

## Reverse / backward order
all_points = []
for track in gpx.tracks:
    for segment in track.segments:
        all_points.extend(segment.points)
reversed_points = list(reversed(all_points))
for chunk in divide_chunks(reversed_points, 10):
            formatted_points = map(lambda p: '({:.4f},{:.4f})'.format(p.latitude, p.longitude), chunk)
            print('            ' + ', '.join(formatted_points) + ',')
