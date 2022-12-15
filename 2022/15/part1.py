import re

f = open("2022/15/test", "r")
input = f.read()


def parsepositions(input):
    sensors = list(map(lambda m: (int(m[0]), int(m[1])), re.findall(
        "Sensor at x=(-?\d+), y=(-?\d+)", input)))
    beacons = list(map(lambda m: (int(m[0]), int(m[1])), re.findall(
        "beacon is at x=(-?\d+), y=(-?\d+)", input)))
    return (sensors, beacons)


def normalizepositions(sensors, beacons):
    minx, maxx, miny, maxy = findminmax(sensors + beacons)
    sensors = list(map(lambda s: (s[0] - minx, s[1] - miny), sensors))
    beacons = list(map(lambda s: (s[0] - minx, s[1] - miny), beacons))
    return (sensors, beacons)


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
# print(sensors, beacons)
sensors, beacons = normalizepositions(sensors, beacons)
# print(sensors, beacons)
minx, maxx, miny, maxy = findminmax(sensors + beacons)
# print(minx, maxx, miny, maxy)
offset = 15

grid = [['.' for _ in range(minx, maxx + offset * 2 + 1)]
        for _ in range(miny, maxy + offset * 2 + 1)]

for sensor in sensors:
    grid[sensor[1] + offset][sensor[0] + offset] = 'S'

for beacon in beacons:
    grid[beacon[1] + offset][beacon[0] + offset] = 'B'


def drawarea(grid, center, d):
    starty = center[1] - d
    endy = center[1] + d
    for y in range(starty, center[1] + 1):
        w = (y - starty) * 2 + 1
        whalf = int(w / 2)
        for x in range(center[0] - whalf, center[0] + whalf + 1):
            if grid[y + offset][x + offset] == '.':
                grid[y + offset][x + offset] = '#'
    for y in range(center[1] + 1, endy + 1):
        w = abs(y - endy) * 2
        whalf = int(w / 2)
        for x in range(center[0] - whalf, center[0] + whalf + 1):
            if grid[y + offset][x + offset] == '.':
                grid[y + offset][x + offset] = '#'
    return grid


printgrid(grid)

for i in range(len(sensors)):
    sensor = sensors[i]
    beacon = beacons[i]
    d = distance(sensor, beacon)
    grid = drawarea(grid, sensor, d)
    # printgrid(grid)

printgrid(grid)
result = len(list(filter(lambda p: p == '#', grid[10 + offset])))
print(result)
