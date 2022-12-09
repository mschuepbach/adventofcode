import math

f = open("2022/09/input", "r")
lines = f.readlines()

posx = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
posy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def parsemove(line):
    x = line.split(" ")
    dir = x[0]
    dist = int(x[1])
    return (dir, dist)


def printfield(posx, posy):
    startx = min(min(posx), 0)
    starty = min(min(posy), 0)
    endx = max(max(posx), 0)
    endy = max(max(posy), 0)
    for y in range(starty, endy + 1):
        line = ""
        for x in range(startx, endx + 1):
            char = "."
            if x == 0 and y == 0:
                char = "s"
            for i in range(9, -1, -1):
                if x == posx[i] and y == posy[i]:
                    if i == 0:
                        char = "H"
                    else:
                        char = str(i)
            line += char
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
printfield(posx, posy)
visited = set()

for line in lines:
    dir, dist = parsemove(line)
    print(f"== {dir} {dist} ==")
    for i in range(dist):
        if dir == "L":
            posx[0] -= 1
        if dir == "U":
            posy[0] -= 1
        if dir == "R":
            posx[0] += 1
        if dir == "D":
            posy[0] += 1
        for i in range(9):
            j = i + 1
            posx[j], posy[j] = calcTpos(posx[i], posy[i], posx[j], posy[j])
        visited.add((posx[9], posy[9]))
        printfield(posx, posy)

print(len(visited))
