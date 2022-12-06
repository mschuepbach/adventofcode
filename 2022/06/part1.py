f = open("2022/06/input", "r")
input = f.read()

a = []
result = 0

for char in input:
    a.append(char)
    result += 1
    if len(a) < 4:
        continue
    if len(set(a)) == 4:
        break
    del a[0]

print(result)
