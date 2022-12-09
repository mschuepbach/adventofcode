import math

f = open("2022/09/input", "r")
lines = f.readlines()

posHx = 0
posHy = 0
posTx = 0
posTy = 0


def parsemove(line):
    x = line.split(" ")
    dir = x[0]
    dist = int(x[1])
    return (dir, dist)


def printfield(posHx, posHy, posTx, posTy):
    startx = min(0, posHx, posTx)
    starty = min(0, posHy, posTy)
    endx = max(0, posHx, posTx)
    endy = max(0, posHy, posTy)
    for y in range(starty, endy + 1):
        line = ""
        for x in range(startx, endx + 1):
            if x == posHx and y == posHy:
                line += "H"
            elif x == posTx and y == posTy:
                line += "T"
            elif x == 0 and y == 0:
                line += "s"
            else:
                line += "."
        print(line)
    print("\n")


def calcTpos(posHx, posHy, posTx, posTy):
    d = math.sqrt((posHx - posTx) ** 2 + (posHy - posTy) ** 2)
    if d >= 2 and abs(posHx - posTx) >= 1:
        posTx += 1 if posHx - posTx > 0 else -1
    if d >= 2 and abs(posHy - posTy) >= 1:
        posTy += 1 if posHy - posTy > 0 else -1
    return (posTx, posTy)


print(f"== Initial State ==")
printfield(posHx, posHy, posTx, posTy)
visited = set()

for line in lines:
    dir, dist = parsemove(line)
    print(f"== {dir} {dist} ==")
    for i in range(dist):
        if dir == "L":
            posHx -= 1
        if dir == "U":
            posHy -= 1
        if dir == "R":
            posHx += 1
        if dir == "D":
            posHy += 1
        posTx, posTy = calcTpos(posHx, posHy, posTx, posTy)
        visited.add((posTx, posTy))
        printfield(posHx, posHy, posTx, posTy)

print(len(visited))
