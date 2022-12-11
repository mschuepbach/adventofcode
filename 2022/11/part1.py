f = open("2022/11/input", "r")
lines = f.readlines()


class Monkey:
    def __init__(self) -> None:
        self.id = None
        self.items = []
        self.op = None
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

for round in range(1, 21):
    for monkey in monkeys:
        print(f"Monkey {monkey.id}:")
        for item in monkey.items:
            print(f"  Monkey inspects an item with a worry level of {item}.")
            monkey.inspected += 1
            new = monkey.op(item)
            print(f"    Worry level is now {new}.")
            new = int(new/3)
            print(
                f"    Monkey gets bored with item. Worry level is divided by 3 to {new}.")
            if new % monkey.test == 0:
                print(
                    f"    Current worry level is divisible by {monkey.test}.")
                print(
                    f"    Item with worry level {new} is thrown to monkey {monkey.iftrue}.")
                monkeys[monkey.iftrue].items.append(new)
            else:
                print(
                    f"    Current worry level is not divisible by {monkey.test}.")
                print(
                    f"    Item with worry level {new} is thrown to monkey {monkey.iffalse}.")
                monkeys[monkey.iffalse].items.append(new)
        monkey.items = []
    print(
        f"After round {round}, the monkeys are holding items with these worry levels:")
    for monkey in monkeys:
        print(f"Monkey {monkey.id}: {monkey.items}")

for monkey in monkeys:
    print(f"Monkey {monkey.id} inspected items {monkey.inspected} times.")

sorted = sorted(list(map(lambda x: x.inspected, monkeys)))
print(sorted[-2] * sorted[-1])
