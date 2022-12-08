f = open("2022/08/input", "r")
lines = f.read().split("\n")[:-1]


def calcscore(start, stop, x, y):
    diff = stop - start
    step = 1 if diff > 0 else -1
    sum = 0
    for i in range(start, stop + step, step):
        othertree = int(lines[y][i] if y > -1 else lines[i][x])
        sum += 1
        if othertree >= tree:
            return sum
    return sum


maxy = len(lines) - 1
maxx = len(lines[0]) - 1
maxscore = 0
for y in range(maxy + 1):
    line = lines[y]
    for x in range(maxx + 1):
        tree = int(line[x])
        if y == 0 or x == 0 or y == maxy or x == maxx:
            continue
        scorel = calcscore(x - 1, 0, -1, y)
        scoret = calcscore(y - 1, 0, x, -1)
        scorer = calcscore(x + 1, maxx, -1, y)
        scoreb = calcscore(y + 1, maxy, x, -1)
        score = scorel * scoret * scorer * scoreb
        if score > maxscore:
            maxscore = score

print(maxscore)
