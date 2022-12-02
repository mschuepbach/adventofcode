f = open("2022/01/input", "r")
lines = f.read()
elves = lines[:-1].split("\n\n")

result = max(map(lambda elve: sum(
    list(map(lambda calories: int(calories), elve.split("\n")))), elves))
print(result)
