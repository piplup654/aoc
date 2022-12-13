#!/usr/bin/env python3
from functools import cmp_to_key
def parseInput(filename):
    with open(filename, "r") as f:
        data = f.read().strip().split("\n\n")
        data = [x.split("\n") for x in data]
        for i in range(len(data)):
            data[i][0] = eval(data[i][0])
            data[i][1] = eval(data[i][1])
        return data
def part1(data):
    answer = 0
    for index, i in enumerate(data):
        pam = handler(i[0], i[1])
        if pam == 1:
            answer += index+1
    return answer
def handler(i1, i2):
    if type(i1) is list and type(i2) is int:
        i2 = [i2]
    elif type(i2) is list and type(i1) is int:
        i1 = [i1]
    if type(i1) is int and type(i2) is int:
        if i1 < i2:
            return 1
        if i1 > i2:
            return -1
        else:
            return 0
    if type(i1) == list and type(i2) == list:
        for j in range(min(len(i1), len(i2))):
            verdict = handler(i1[j], i2[j])
            if verdict != 0:
                return verdict
        if len(i1) < len(i2):
            return 1
        if len(i1) > len(i2):
            return -1
        return 0
def part2(data):
    flatenned_data = [item for sublist in data for item in sublist]
    position_1 = 1
    position_2 = 2
    for p in flatenned_data:
        if handler(p, [[2]]) == 1:
            position_1 += 1
            position_2 += 1
        elif handler(p, [[6]]) == 1:
            position_2 += 1
    return position_1 * position_2
def part2_2(data):
    flatenned_data = [item for sublist in data for item in sublist]
    flatenned_data.append([[2]])
    flatenned_data.append([[6]])
    flatenned_data = sorted(flatenned_data, key=cmp_to_key(handler), reverse=True)
    ans = list()
    for index, i in enumerate(flatenned_data):
        if i == [[2]]:
            ans.append(index+1)
        if i == [[6]]:
            ans.append(index+1)
    return ans[0]*ans[1]
inp = parseInput("input.txt")
print(part1(inp), part2(inp), part2_2(inp))