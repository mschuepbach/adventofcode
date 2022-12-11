f = open("2022/11/input", "r")
lines = f.readlines()


class Monkey:
    def __init__(self) -> None:
        self.id = None
        self.items = []
        self.a = None
        self.op = None
        self.b = None
        self.test = None
        self.iftrue = None
        self.iffalse = None
        self.inspected = 0


def eval(a, op, b):
    if op == "+":
        return a + b
    elif op == "*":
        return a * b
    else:
        raise NotImplementedError(f"Operation {op} is not supported.")


monkeys = []
monkey = None

for line in lines:
    if line.startswith("Monkey"):
        monkey = Monkey()
        monkey.id = int(line.split(" ")[1][:-2])
        monkeys.append(monkey)
    elif line.startswith("  Starting items"):
        monkey.items = list(map(lambda x: int(x), line[18:-1].split(", ")))
    elif line.startswith("  Operation"):
        tokens = line[19:-1].split(" ")
        monkey.op = lambda old, _t=tokens: eval(old if _t[0] == "old" else int(
            _t[0]), _t[1], old if _t[2] == "old" else int(_t[2]))
    elif line.startswith("  Test"):
        monkey.test = int(line[21:-1])
    elif line.startswith("    If true"):
        monkey.iftrue = int(line[29:-1])
    elif line.startswith("    If false"):
        monkey.iffalse = int(line[29:-1])

lcm = 1
for monkey in monkeys:
    lcm *= monkey.test

for round in range(1, 10_001):
    for monkey in monkeys:
        for item in monkey.items:
            monkey.inspected += 1
            new = monkey.op(item % lcm)
            if new % monkey.test == 0:
                monkeys[monkey.iftrue].items.append(new)
            else:
                monkeys[monkey.iffalse].items.append(new)
        monkey.items = []

sorted = sorted(list(map(lambda x: x.inspected, monkeys)))
print(sorted[-2] * sorted[-1])
