def parseInput(filename):
    with open(filename, "r") as file:
        return [x.strip().split() for x in file]
# ROCK - 1, PAPER - 2, SCISSOR - 3
# WIN - 6, DRAW - 3, LOSS - 0
# A - ROCK, B - PAPER, C - Scissors
# X - ROCK, Y -  PAPER, Z - Scissors
points_dict = {"AX": 4, "AY": 8, "AZ": 3, "BX": 1, "BY": 5, "BZ": 9, "CX": 7, "CY": 2, "CZ": 6}
win_dicts = {"AY": 4, "AX": 3, "AZ": 8, "BX": 1, "BY": 5, "BZ": 9, "CX": 2, "CY": 6, "CZ": 7}
def partA(data):
    points = 0
    for i in data:
        points += points_dict[f"{i[0]}{i[1]}"]
    return points
def partB(data):
    points = 0
    for i in data:
        points += win_dicts[f"{i[0]}{i[1]}"]
    return points
print(partA(parseInput("input.txt")))
print(partB(parseInput("input.txt")))
