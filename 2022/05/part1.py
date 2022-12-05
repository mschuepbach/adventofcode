f = open("2022/05/input", "r")
lines = f.readlines()

stacks = [
    ["T","R","G","W","Q","M","F","P"][::-1],
    ["R","F","H"][::-1],
    ["D","S","H","G","V","R","Z","P"][::-1],
    ["G","W","F","B","P","H","Q"][::-1],
    ["H","J","M","S","P"][::-1],
    ["L","P","R","S","H","T","Z","M"][::-1],
    ["L","M","N","H","T","P"][::-1],
    ["R","Q","D","F"][::-1],
    ["H","P","L","N","C","S","D"][::-1],
]

moves = lines[10:]

def moveCreates(line):
    words = line.split(" ")
    nCreates = int(words[1])
    fromStack = int(words[3])
    toStack = int(words[5])
    for i in range(nCreates):
        create = stacks[fromStack - 1].pop()
        stacks[toStack - 1].append(create)

for move in moves:
    moveCreates(move)

result = ""

for stack in stacks:
    result += stack.pop()

print(result)
