import json

f = open("2022/13/input", "r")
lines = f.readlines()


def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return 1
        if a > b:
            return -1
        return 0
    elif isinstance(a, list) and isinstance(b, list):
        la = len(a)
        lb = len(b)
        for i in range(min(la, lb)):
            result = compare(a[i], b[i])
            if result != 0:
                return result
        if la == lb:
            return 0
        if la < lb:
            return 1
        return -1
    elif isinstance(a, int):
        return compare([a], b)
    return compare(a, [b])


npairs = int((len(lines) + 1) / 3)
sum = 0

for i in range(npairs):
    a = json.loads(lines[i * 3])
    b = json.loads(lines[i * 3 + 1])
    result = compare(a, b)
    if result == 1:
        sum += i + 1

print(sum)
