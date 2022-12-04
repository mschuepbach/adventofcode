f = open("2022/04/input", "r")
lines = f.readlines()


def overlaps(line):
    sections = line.split(",")
    a = sections[0].split("-")
    b = sections[1].split("-")
    a_start = int(a[0])
    a_end = int(a[1])
    b_start = int(b[0])
    b_end = int(b[1])
    return (a_start <= b_end and a_end >= b_start) or (b_start <= a_end and b_end >= a_start)


result = len(list(filter(lambda l: overlaps(l), lines)))

print(result)
