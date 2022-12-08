f = open("2022/08/input", "r")
lines = f.read().split("\n")[:-1]


def isvisible(start, stop, x, y):
    for i in range(start, stop + 1):
        othertree = int(lines[y][i] if y > -1 else lines[i][x])
        if othertree >= tree:
            return False
    return True


maxy = len(lines) - 1
maxx = len(lines[0]) - 1
sum = 0
for y in range(maxy + 1):
    line = lines[y]
    for x in range(maxx + 1):
        tree = int(line[x])
        if y == 0 or x == 0 or y == maxy or x == maxx:
            sum += 1
            continue
        if isvisible(0, x - 1, -1, y):
            sum += 1
            continue
        if isvisible(0, y - 1, x, -1):
            sum += 1
            continue
        if isvisible(x + 1, maxx, -1, y):
            sum += 1
            continue
        if isvisible(y + 1, maxy, x, -1):
            sum += 1

print(sum)
