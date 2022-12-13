import math

f = open("2022/12/input", "r")
lines = list(map(lambda l: l[:-1], f.readlines()))


def visitableneighbors(heightmap, x, y):
    width = len(heightmap[0])
    height = len(heightmap)
    positions = [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]
    visitable = []
    for posx, posy in positions:
        if posx < 0 or posx >= width or posy < 0 or posy >= height:
            continue
        if heightmap[posy][posx] - heightmap[y][x] <= 1:
            visitable.append((posx, posy))
    return visitable


def reconstructpath(camefrom: dict, current):
    totalpath = [current]
    while current in camefrom.keys():
        current = camefrom[current]
        totalpath = [current] + totalpath
    return totalpath


def findminfscore(nodes, fscore):
    min = math.inf
    minnode = None
    for node in nodes:
        if fscore[node] < min:
            min = fscore[node]
            minnode = node
    return minnode


def h(node, goal):
    return math.sqrt((goal[0] - node[0]) ** 2 + (goal[1] - node[1]) ** 2)


def getnodes(heightmap):
    width = len(heightmap[0])
    height = len(heightmap)
    nodes = []
    for y in range(height):
        for x in range(width):
            nodes.append((x, y))
    return nodes


def astar(heightmap, start, goal, h):
    openset = [start]
    camefrom = {}
    gscore = {key: math.inf for key in getnodes(heightmap)}
    gscore[start] = 0
    fscore = {key: math.inf for key in getnodes(heightmap)}
    fscore[start] = h(start, goal)

    while len(openset) > 0:
        current = findminfscore(openset, fscore)
        if current[0] == goal[0] and current[1] == goal[1]:
            return reconstructpath(camefrom, current)
        openset.remove(current)
        for neighbor in visitableneighbors(heightmap, current[0], current[1]):
            tentativegscore = gscore[current] + 1
            if tentativegscore < gscore[neighbor]:
                camefrom[neighbor] = current
                gscore[neighbor] = tentativegscore
                fscore[neighbor] = tentativegscore + h(neighbor, goal)
                if neighbor not in openset:
                    openset.append(neighbor)
    raise RuntimeError("Could not reach goal")


width = len(lines[0])
height = len(lines)
heightmap = [[-1 for _ in range(width)] for _ in range(height)]
start = None
destination = None

for y in range(height):
    for x in range(width):
        character = lines[y][x]
        if character == 'S':
            start = (x, y)
            character = 'a'
        elif character == 'E':
            destination = (x, y)
            character = 'z'
        heightmap[y][x] = ord(character) - 97

path = astar(heightmap, start, destination, h)
print(len(path) - 1)
