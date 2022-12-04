f = open("2022/04/input", "r")
lines = f.readlines()


def fullyContains(line):
    sections = line.split(",")
    a = sections[0].split("-")
    b = sections[1].split("-")
    a_start = int(a[0])
    a_end = int(a[1])
    b_start = int(b[0])
    b_end = int(b[1])
    return (a_start >= b_start and a_end <= b_end) or (b_start >= a_start and b_end <= a_end)


result = len(list(filter(lambda l: fullyContains(l), lines)))

print(result)
