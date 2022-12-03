f = open("2022/03/input", "r")
lines = f.readlines()


def points(char):
    ascii = ord(char)
    if ascii >= 97:
        return ascii - 96
    return ascii - 64 + 26


def findItem(items1, items2, items3):
    items1 = set(items1)
    items2 = set(items2)
    items3 = set(items3)
    items1and2 = set()
    for item1 in items1:
        for item2 in items2:
            if item1 == item2:
                items1and2.add(item1)
    for item3 in items3:
        for item1and2 in items1and2:
            if item3 == item1and2:
                return item3
    raise RuntimeError("item not found!")


result = 0

for groupIdx in range(0, len(lines), 3):
    items1 = lines[groupIdx][:-1]
    items2 = lines[groupIdx + 1][:-1]
    items3 = lines[groupIdx + 2][:-1]
    result += points(findItem(items1, items2, items3))

print(result)
