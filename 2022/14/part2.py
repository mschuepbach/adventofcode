import re

f = open("2022/14/input", "r")
input = f.read()


def findminmax(input):
    x = list(map(lambda m: int(m[:-1]), re.findall("\d+,", input)))
    y = list(map(lambda m: int(m[1:]), re.findall(",\d+", input)))
    return (min(x), max(x), min(y), max(y))


def printcave(cave):
    for row in cave:
        print(''.join(row))
    print('\n')


def line(a, b):
    start = a if a < b else b
    end = a if a > b else b
    return [i for i in range(start, end + 1)]


rockpaths = list(map(lambda l: l.split(" -> "), input[:-1].split("\n")))
minx, maxx, miny, maxy = findminmax(input)
maxedgex = 1000
cave = [['.' for _ in range(0, maxedgex)] for _ in range(0, maxy + 3)]

for i in range(len(rockpaths)):
    for j in range(len(rockpaths[i]) - 1):
        a = rockpaths[i][j].split(',')
        b = rockpaths[i][j + 1].split(',')
        xa = int(a[0])
        ya = int(a[1])
        xb = int(b[0])
        yb = int(b[1])
        lx = line(xa, xb)
        ly = line(ya, yb)
        for x in lx:
            cave[ya][x] = '#'
        for y in ly:
            cave[y][xa] = '#'

for x in range(0, maxedgex):
    cave[maxy + 2][x] = '#'

reachedege = False
reachedtop = False
n = 0

printcave(cave)

while not reachedege and not reachedtop:
    sandposx = 500
    sandposy = 0
    canfall = True
    n += 1

    while canfall:
        if sandposx < 0 or sandposx > maxedgex:
            reachedege = True
            break
        if cave[sandposy + 1][sandposx] == '.':
            sandposy += 1
        elif cave[sandposy + 1][sandposx - 1] == '.':
            sandposy += 1
            sandposx -= 1
        elif cave[sandposy + 1][sandposx + 1] == '.':
            sandposy += 1
            sandposx += 1
        else:
            canfall = False
            cave[sandposy][sandposx] = 'o'
            if sandposy == 0:
                reachedtop = True

printcave(cave)
print(n)
