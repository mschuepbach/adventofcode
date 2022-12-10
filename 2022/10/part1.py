f = open("2022/10/input", "r")
lines = f.readlines()

x = 1
cycle = 1
signals = []

for line in lines:
    if (cycle - 20) % 40 == 0:
        signals.append(cycle * x)
    split = line.split(" ")
    cycle += 1
    if split[0].startswith("noop"):
        continue
    if (cycle - 20) % 40 == 0:
        signals.append(cycle * x)
    x += int(split[1])
    cycle += 1

print(sum(signals))
