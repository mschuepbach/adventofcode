f = open("2022/03/input", "r")
lines = f.readlines()


def points(char):
    ascii = ord(char)
    if ascii >= 97:
        return ascii - 96
    return ascii - 64 + 26


def findItem(items):
    itemsPerCompartment = int(len(items) / 2)
    compartment1 = set(items[:itemsPerCompartment])
    compartment2 = set(items[itemsPerCompartment:])
    for item1 in compartment1:
        for item2 in compartment2:
            if item1 == item2:
                return item1
    raise RuntimeError("item not found!")


result = sum(map(lambda l: points(findItem(l[:-1])), lines))

print(result)
