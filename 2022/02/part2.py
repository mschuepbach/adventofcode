f = open("2022/02/input", "r")
lines = f.readlines()


def points(enemy, gameEnd):
    if gameEnd == "Y":
        return enemy  # draw
    if (enemy == 2 and gameEnd == "X") or (enemy == 3 and gameEnd == "Z"):
        return 1  # rock
    if (enemy == 1 and gameEnd == "Z") or (enemy == 3 and gameEnd == "X"):
        return 2  # paper
    return 3  # scissors


enemyMapping = {"A": 1, "B": 2, "C": 3}
pointsMapping = {"X": 0, "Y": 3, "Z": 6}
result = sum(map(lambda l: points(
    enemyMapping[l[0]], l[2]) + pointsMapping[l[2]], lines))

print(result)
