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
cave = [['.' for _ in range(minx, maxx + 1)] for _ in range(0, maxy + 1)]

for i in range(len(rockpaths)):
    for j in range(len(rockpaths[i]) - 1):
        a = rockpaths[i][j].split(',')
        b = rockpaths[i][j + 1].split(',')
        xa = int(a[0]) - minx
        ya = int(a[1])
        xb = int(b[0]) - minx
        yb = int(b[1])
        lx = line(xa, xb)
        ly = line(ya, yb)
        for x in lx:
            cave[ya][x] = '#'
        for y in ly:
            cave[y][xa] = '#'

reachedege = False
n = 0

printcave(cave)

while not reachedege:
    sandposx = 500 - minx
    sandposy = 0
    canfall = True
    n += 1

    while canfall:
        if sandposx < 0 or sandposx > maxx - minx or sandposy >= maxy:
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

printcave(cave)
print(n - 1)
