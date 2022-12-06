def parse_input(filename):
    with open(filename, "r") as file:
        return file.read().strip()
def part1(data):
    for i in range(len(data)):
        if i - 3 > 0:
            marker = len(set([data[i], data[i-1], data[i-2], data[i-3]]))
            if marker == 4:
                return i+1
def part2(data):
    for i in range(len(data)):
        if i -13 > 0:
            marker = len(set([data[i-j] for j in range(14)]))
            if marker == 14:
                return i+1
print(part1(parse_input("input.txt")))
print(part2(parse_input("input.txt")))
