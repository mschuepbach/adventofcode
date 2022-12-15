import re

f = open("2022/15/input", "r")
input = f.read()


def parsepositions(input):
    sensors = list(map(lambda m: (int(m[0]), int(m[1])), re.findall(
        "Sensor at x=(-?\d+), y=(-?\d+)", input)))
    beacons = list(map(lambda m: (int(m[0]), int(m[1])), re.findall(
        "beacon is at x=(-?\d+), y=(-?\d+)", input)))
    return (sensors, beacons)


def normalizepositions(sensors, beacons, row):
    minx, maxx, miny, maxy = findminmax(sensors + beacons)
    sensors = list(map(lambda s: (s[0] - minx, s[1] - miny), sensors))
    beacons = list(map(lambda s: (s[0] - minx, s[1] - miny), beacons))
    row -= miny
    return (sensors, beacons, row)


def findminmax(positions):
    x = list(map(lambda p: p[0], positions))
    y = list(map(lambda p: p[1], positions))
    return (min(x), max(x), min(y), max(y))


def printgrid(grid):
    for row in grid:
        print(''.join(row))
    print('\n')


def distance(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


sensors, beacons = parsepositions(input)
row = 2000000
sensors, beacons, row = normalizepositions(sensors, beacons, row)
minx, maxx, miny, maxy = findminmax(sensors + beacons)
offset = 1780271 # max distance for offset

line = ['.' for _ in range(minx, maxx + offset * 2 + 1)]

for sensor in sensors:
    if sensor[1] == row:
        line[sensor[0] + offset] = 'S'

for beacon in beacons:
    if beacon[1] == row:
        line[beacon[0] + offset] = 'B'

def drawarea(line, center, d):
    starty = center[1] - d
    endy = center[1] + d
    for y in range(starty, center[1] + 1):
        if y != row:
            continue
        w = (y - starty) * 2 + 1
        whalf = int(w / 2)
        for x in range(center[0] - whalf, center[0] + whalf + 1):
            if line[x + offset] == '.':
                line[x + offset] = '#'
    for y in range(center[1] + 1, endy + 1):
        if y != row:
            continue
        w = abs(y - endy) * 2
        whalf = int(w / 2)
        for x in range(center[0] - whalf, center[0] + whalf + 1):
            if line[x + offset] == '.':
                line[x + offset] = '#'
    return line


# printgrid(grid)

for i in range(len(sensors)):
    sensor = sensors[i]
    beacon = beacons[i]
    d = distance(sensor, beacon)
    line = drawarea(line, sensor, d)
    # printgrid(grid)

# printgrid(grid)
result = len(list(filter(lambda p: p == '#', line)))
print(result)
