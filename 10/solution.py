from dataclasses import dataclass
def parse_input(filename):
    with open(filename, "r") as file:
        return [x.strip().split() for x in file]
def part1(data):
    X = 1
    cycle = 0
    visit_cycles = [20,60,100,140,180,220]
    cycle_vals = []
    for i in data:
        if i[0] == "noop":
            cycle += 1
        else:
            for j in range(2):
                cycle += 1
                if cycle in visit_cycles:
                    cycle_vals.append(X*cycle)
                    visit_cycles.remove(cycle)
                if j == 1:
                    X += int(i[1])
        if cycle in visit_cycles:
            cycle_vals.append(X*cycle)
            visit_cycles.remove(cycle)
    return sum(cycle_vals)
@dataclass
class Sprite:
    left: int
    middle: int
    right: int
    def change_position(self, new_position):
        self.middle = new_position
        self.left = new_position-1
        self.right = new_position+1
    def get_position_array(self):
        return [self.left, self.middle, self.right]
def part2(data):
    X = 1
    cycle = 0
    row = 0
    column = 0
    CRT = [["." for _ in range(40)] for _ in range(6)]
    sprite = Sprite(0,1,2)
    for i in data:
        if i[0] == "noop":
            row = (cycle%40)
            cycle += 1
            if row in sprite.get_position_array(): CRT[column][row] = "#"
            if row >= 39 and column < 5:
                if column < 5:
                    column += 1
        else:
            for j in range(2):
                row = (cycle%40)
                cycle += 1
                if row in sprite.get_position_array(): CRT[column][row] = "#"
                if row >= 39 and column < 5:
                    if column < 5:
                        column += 1
                if j == 1:
                    X += int(i[1])
                    sprite.change_position(X)
    return CRT
print(part1(parse_input("input.txt")))
pam = part2(parse_input("input.txt"))
[print(x) for x in pam]