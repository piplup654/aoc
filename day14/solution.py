import time
def parse_input(filename):
    with open(filename, "r") as f:
        filled = set()
        for line in f.readlines():
            coordinates = list(map(lambda coordinate: list(map(int, coordinate.split(","))), line.split(" -> ")))
            for i in range(1,len(coordinates)):
                cx, cy = coordinates[i]
                px, py = coordinates[i-1]
                if cy != py:
                    for y in range(min(cy,py), max(cy,py)+1):
                        filled.add((cx,y))
                if cx != px:
                    for x in range(min(cx,px), max(cx,px)+1):
                        filled.add((x,cy))
        return filled
def get_possible_ways_for_falling(sand_point, cave_system):
    possibilities = [[sand_point[0], sand_point[1]+1],
                     [sand_point[0]-1, sand_point[1]+1],
                     [sand_point[0]+1, sand_point[1]+1]]
    checked_possibility = list()
    for i in range(len(possibilities)):
        if possibilities[i] not in cave_system:
            checked_possibility.append(possibilities[i])
    if checked_possibility:
        return list(checked_possibility[0])
    else:
        return 0
def part1(data):
    sand_start_point = [500,0]
    used_space = list(data)
    used_space = list(map(list, used_space))
    only_sand_space = [sand_start_point]
    max_Y = 0
    for i in used_space:
        if i[1] > max_Y:
            max_Y = i[1]
    for i in range(1000):
        current_sand_system = [sand_start_point]
        while get_possible_ways_for_falling(current_sand_system[-1], used_space) != 0:
            new_block = get_possible_ways_for_falling(current_sand_system[-1], used_space)
            current_sand_system.append(new_block)
            if current_sand_system[-1][1] >= max_Y:
                return len(only_sand_space[1:])
        used_space.append(current_sand_system[-1])
        only_sand_space.append(current_sand_system[-1])
    return len(only_sand_space[1:])
def sandFalling(used_space):
    x,y = 500, 0
    if [x,y] in used_space:
        return [x,y]
    while y <= max_Y:
        if get_possible_ways_for_falling([x,y], used_space):
            x,y = get_possible_ways_for_falling([x,y], used_space)
        else:
            break
    return [x,y]
def part2(data):
    used_space = list(data)
    used_space = list(map(list, used_space))
    global max_Y
    max_Y = sorted(used_space, key=lambda x: x[1], reverse=True)[0][1]+2
    ans = 0
    while True:
        x,y = sandFalling(used_space)
        used_space.append([x,y])
        ans += 1
        print(ans)
        if [x,y] == [500,0]:
            break
    return ans
print(part2(parse_input("input.txt")))