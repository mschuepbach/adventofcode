f = open("2022/02/input", "r")
lines = f.readlines()


def points(enemy, me):
    if enemy == me:
        return 3  # draw
    if (me == 1 and enemy == 3) or (me == 3 and enemy == 2) or (me == 2 and enemy == 1):
        return 6  # win
    return 0  # lost


enemyMapping = {"A": 1, "B": 2, "C": 3}
myMapping = {"X": 1, "Y": 2, "Z": 3}
result = sum(map(lambda l: points(
    enemyMapping[l[0]], myMapping[l[2]]) + myMapping[l[2]], lines))

print(result)
