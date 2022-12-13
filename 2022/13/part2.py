import json
from functools import cmp_to_key

packets = open("2022/13/input", "r")
lines = packets.readlines()


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


lines = list(filter(lambda l: l != "\n", lines))
packets = list(map(lambda l: json.loads(l), lines))
packets.append([[2]])
packets.append([[6]])
packets = sorted(packets, key=cmp_to_key(compare), reverse=True)

print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))
