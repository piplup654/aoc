# if in the same row or column and two steps difference follow normally
# if not in the same row col, follow diagonally one move
# func that makes the choice how to follow a head input
import copy
from dataclasses import dataclass
@dataclass
class RopePart:
    X: int
    Y: int
    def __copy__(self):
        return RopePart(copy.copy(self.X), copy.copy(self.Y))
def parse_input(filename):
    with open(filename, "r") as file:
        return [x.strip().split() for x in file]
def followHead2(head: RopePart, tail: RopePart):
    new_tail_pos = tail.__copy__()
    if (abs(head.X-tail.X) > 1) or (abs(head.Y - tail.Y) > 1):
        if head.X != tail.X and head.Y != tail.Y:
            difference_X = head.X - tail.X
            if difference_X > 0:
                new_tail_pos.X += 1
            else:
                new_tail_pos.X -= 1
            difference_Y = head.Y - tail.Y
            if difference_Y > 0:
                new_tail_pos.Y += 1
            else:
                new_tail_pos.Y -= 1
        elif (head.X != tail.X and head.Y == tail.Y) or (head.Y != tail.Y and head.X == head.X):
            if head.X == tail.X:
                difference = head.Y - new_tail_pos.Y
                if difference > 0:
                    new_tail_pos.Y += 1
                else:
                    new_tail_pos.Y -= 1
            if head.Y == tail.Y:
                difference = head.X - new_tail_pos.X
                if difference > 0:
                    new_tail_pos.X += 1
                else:
                    new_tail_pos.X -= 1
    return new_tail_pos
def part1(data):
    head = RopePart(1,1)
    tail = RopePart(1,1)
    unique_positions = set()
    for i in data:
        command = i[0]
        value = int(i[1])
        match command:
            case "U":
                for _ in range(value):
                    head.Y += 1
                    tail = followHead2(head, tail)
                    unique_positions.add((tail.X, tail.Y))
            case "D":
                for _ in range(value):
                    head.Y -= 1
                    tail = followHead2(head, tail)
                    unique_positions.add((tail.X, tail.Y))
            case "R":
                for _ in range(value):
                    head.X += 1
                    tail = followHead2(head, tail)
                    unique_positions.add((tail.X, tail.Y))
            case "L":
                for _ in range(value):
                    head.X -= 1
                    tail = followHead2(head, tail)
                    unique_positions.add((tail.X, tail.Y))
    return len(unique_positions)
def part2(data):
    head = RopePart(1,1)
    knots = [RopePart(1,1) for x in range(9)]
    unique_positions = set()
    for i in data:
        command = i[0]
        value = int(i[1])
        match command:
            case "U":
                for _ in range(value):
                    head.Y += 1
                    for index in range(len(knots)):
                        if index == 0:
                            new_tail_pos = followHead2(head, knots[index])
                            knots[index] = new_tail_pos
                        else:
                            new_tail_pos = followHead2(knots[index-1], knots[index])
                            knots[index] = new_tail_pos
                            if index == 8:
                                unique_positions.add((knots[index].X, knots[index].Y))
            case "D":
                for _ in range(value):
                    head.Y -= 1
                    for index in range(len(knots)):
                        if index == 0:
                            new_tail_pos = followHead2(head, knots[index])
                            knots[index] = new_tail_pos
                        else:
                            new_tail_pos = followHead2(knots[index-1], knots[index])
                            knots[index] = new_tail_pos
                            if index == 8:
                                unique_positions.add((knots[index].X, knots[index].Y))
            case "R":
                for _ in range(value):
                    head.X += 1
                    for index in range(len(knots)):
                        if index == 0:
                            new_tail_pos = followHead2(head, knots[index])
                            knots[index] = new_tail_pos
                        else:
                            new_tail_pos = followHead2(knots[index-1], knots[index])
                            knots[index] = new_tail_pos
                            if index == 8:
                                unique_positions.add((knots[index].X, knots[index].Y))
            case "L":
                for _ in range(value):
                    head.X -= 1
                    for index in range(len(knots)):
                        if index == 0:
                            new_tail_pos = followHead2(head, knots[index])
                            knots[index] = new_tail_pos
                        else:
                            new_tail_pos = followHead2(knots[index-1], knots[index])
                            knots[index] = new_tail_pos
                            if index == 8:
                                unique_positions.add((knots[index].X, knots[index].Y))
    return len(unique_positions)
print(part1(parse_input("input.txt")))
print(part2(parse_input("input.txt")))