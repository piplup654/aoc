from functools import reduce
def parse_input(filename):
    with open(filename, "r") as file: return [[int(y) for y in x.strip()] for x in file]
def part1(data):
    counter = 0
    for i in range(len(data)):
        for j in range(len(data)):
            if i == 0 or j == 0 or i == len(data)-1 or j == len(data[i])-1:
                counter += 1
            else:
                current_tree = data[i][j]
                visible_scores = [True for x in range(4)]
                for z in range(len(data[:i])):
                    if data[z][j] >= current_tree:
                        visible_scores[0] = False
                for z in range(len(data[i:])):
                    if z != 0:
                        if data[z+i][j] >= current_tree:
                            visible_scores[1] = False
                for z in range(len(data[i][j:])):
                    if z != 0:
                        if data[i][z+j] >= current_tree:
                            visible_scores[2] = False
                for z in range(len(data[i][:j])):
                    if data[i][z] >= current_tree:
                        visible_scores[3] = False
                final = list(filter(lambda x: x == True, visible_scores))
                if len(final) > 0:
                    counter += 1
    return counter
def part2(data):
    max_scenic_score = 0
    for i in range(len(data)):
        for j in range(len(data)):
            view_scores = [0 for _ in range(4)]
            if i == 0 or j == 0 or i == len(data)-1 or j == len(data[i])-1:
                pass
            else:
                current_tree = data[i][j]
                for z in range(len(data[:i])):
                    if data[len(data[:i])-1-z][j] >= current_tree:
                        view_scores[0] += 1
                        break
                    else:
                        view_scores[0] += 1
                for z in range(len(data[i:])):
                    if z != 0:
                        if data[z+i][j] >= current_tree:
                            view_scores[1] += 1
                            break
                        else:
                            view_scores[1] += 1
                for z in range(len(data[i][j:])):
                    if z != 0:
                        if data[i][z+j] >= current_tree:
                            view_scores[2] += 1
                            break
                        else:
                            view_scores[2] += 1
                for z in range(len(data[i][:j])):
                    if data[i][len(data[i][:j])-1-z] >= current_tree:
                        view_scores[3] += 1
                        break
                    else:
                        view_scores[3] += 1
                scenic_score = reduce(lambda x,b: x*b, view_scores)
                print(view_scores,current_tree)
                if scenic_score > max_scenic_score:
                    max_scenic_score = scenic_score
    return max_scenic_score
print(part1(parse_input("input.txt")))
print(part2(parse_input("input.txt")))