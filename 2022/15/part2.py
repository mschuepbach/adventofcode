import random
import re

from shapely.geometry import LineString

f = open("2022/15/input", "r")
input = f.read()
f.close()


def parsepositions(input):
    sensors = list(map(lambda m: (int(m[0]), int(m[1])), re.findall(
        "Sensor at x=(-?\d+), y=(-?\d+)", input)))
    beacons = list(map(lambda m: (int(m[0]), int(m[1])), re.findall(
        "beacon is at x=(-?\d+), y=(-?\d+)", input)))
    return (sensors, beacons)


def savesvg(svg):
    file = open("2022/15/grid.html", "w")
    file.write(svg)
    file.close()


def distance(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


def unzip(x):
    return zip(*x)


sensors, beacons = parsepositions(input)

# sort by y then by x pos
sensors, beacons = unzip(
    sorted(list(zip(sensors, beacons)), key=lambda x: (x[0][1], x[0][0])))

maxsearch = 4000000
offset = 100000
svg = f'<html><body><svg width="100%" viewBox="-{offset} -{offset} {maxsearch + offset * 2} {maxsearch + offset * 2}">'

edges = [((0, 0), (0, 0)) for _ in range(len(sensors))]


def r(): return random.randint(0, 255)


for i in range(len(sensors)):
    sensor = sensors[i]
    beacon = beacons[i]
    d = distance(sensor, beacon)
    fillcolor = '#%02X%02X%02X' % (r(), r(), r())
    strokecolor = '#%02X%02X%02X' % (r(), r(), r())
    x = sensor[0]
    y = sensor[1]
    edges[i] = [((x, y-d), (x+d, y)), ((x+d, y), (x, y+d)),
                ((x, y+d), (x-d, y)), ((x-d, y), (x, y-d))]
    svg += f'<polygon points="{x},{y-d} {x+d},{y} {x},{y+d} {x-d},{y}" style="fill:{fillcolor};stroke:{strokecolor};stroke-width:0" opacity="0.5" />'
    svg += f'<line x1="{x}" y1="{y}" x2="{beacon[0]}" y2="{beacon[1]}" style="stroke:blue;stroke-width:2000" />'
    svg += f'<circle cx="{x}" cy="{y}" r="5000" fill="green" />'

intersections = set()

for i in range(len(sensors)):
    for j in range(len(sensors)):
        if i == j:
            continue
        a = sensors[i]
        b = sensors[j]
        edgesa = edges[i]
        edgesb = edges[j]
        for edgea in edgesa:
            for edgeb in edgesb:
                linea = LineString([*edgea])
                lineb = LineString([*edgeb])
                intersection = linea.intersection(lineb)
                if not intersection.is_empty and not isinstance(intersection, LineString):
                    intersections.add((intersection.x, intersection.y))

for i in intersections:
    svg += f'<circle cx="{i[0]}" cy="{i[1]}" r="5000" fill="orange" />'

intersections = list(intersections)
close_intersections = {}

for i in range(len(intersections)):
    for j in range(len(intersections)):
        if i == j:
            continue
        d = distance(intersections[i], intersections[j])
        if d <= 2:
            svg += f'<circle cx="{intersections[i][0]}" cy="{intersections[i][1]}" r="2" fill="red" />'
            if intersections[i] in close_intersections:
                close_intersections[intersections[i]] += 1
            else:
                close_intersections[intersections[i]] = 1
            if intersections[j] in close_intersections:
                close_intersections[intersections[j]] += 1
            else:
                close_intersections[intersections[j]] = 1

intersections_around_beacon = []

for intersection, n_nearby in close_intersections.items():
    if n_nearby >= 6:
        intersections_around_beacon.append(intersection)

x = min(map(lambda i: round(i[0]), intersections_around_beacon)) + 1
y = min(map(lambda i: round(i[1]), intersections_around_beacon)) + 1

frequency = x * maxsearch + y

print(frequency)

svg += f'<polyline points="0,0 {maxsearch},0 {maxsearch},{maxsearch} 0,{maxsearch} 0,0" style="fill:none;stroke:black;stroke-width:2000" />'
svg += '</svg></body></html>'
savesvg(svg)
