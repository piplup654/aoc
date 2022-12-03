def parseInput(filename):
    with open(filename, "r") as file:
        data = file.read().strip().split("\n\n")
        data = [x.strip().split("\n") for x in data]
    return data
data = parseInput("input.txt")
print(sorted([sum(map(lambda x: int(x), x)) for x in data], reverse=True)[:3])