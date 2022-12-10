f = open("2022/10/input", "r")
lines = f.readlines()

x = 1
cycle = 1
rows = []
currentrow = ""


def rendersprite(x):
    start = x - 1
    sprite = list("........................................")
    sprite[start] = "###"
    return "".join(sprite)


for line in lines:
    instruction = line[:-1]
    sprite = rendersprite(x)
    print(f"Sprite position: {sprite}\n")
    print(f"Start cycle  {cycle}: begin executing {instruction}")
    pos = (cycle - 1) % 40
    if pos == 0:
        rows.append(currentrow)
        currentrow = ""
    split = instruction.split(" ")
    print(f"During cycle {cycle}: CRT draws pixel in position {pos}")
    currentrow += sprite[pos]
    print(f"Current CRT row: {currentrow}\n")
    cycle += 1
    if split[0].startswith("noop"):
        continue
    
    pos = (cycle - 1) % 40
    if pos == 0:
        rows.append(currentrow)
        currentrow = ""
    print(f"During cycle {cycle}: CRT draws pixel in position {pos}")
    currentrow += sprite[pos]
    print(f"Current CRT row: {currentrow}")
    x += int(split[1])
    print(
        f"End of cycle {cycle}: finish executing {instruction} (Register X is now {x})")
    cycle += 1

rows.append(currentrow)

for row in rows:
    print(row)
