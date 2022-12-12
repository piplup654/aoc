## advent of code 2022
## https://adventofcode.com/2022
## day 05
def parse_input(lines):
    with open(lines, "r") as file:
        data1 = file.read().split("\n\n")
        orders = map(lambda x: x.split(), data1[1].split("\n"))
        orders = [[y for y in x if y.isalpha() is False] for x in orders]
        data1 = data1[0].split("\n")
        new_data = list()
        max_len = 0
        for i in data1:
            if len(i) > max_len:
                max_len = len(i)
        for j in range(len(data1[:len(data1)-1])):
            pam = data1[j]
            while len(pam) != max_len:
                pam += " "
            new_data.append(pam)
        final_input = list()
        for z in range(len(new_data[0])):
            temp = list()
            for y in range(len(new_data)):
                temp.append(new_data[y][z])
            letts_count = 0
            for i in temp:
                if i.isalpha() and i.isupper():
                    letts_count += 1
            good_temp = list()
            if letts_count >= 1:
                for j in temp:
                    if j.isupper() and j.isalpha():
                        good_temp.append(j)
            if len(good_temp) != 0:
                final_input.append(good_temp)
        return final_input, orders
def part1(data):
    orders = [[int(y) for y in x]for x in data[1]]
    crates = data[0]
    for i in orders:
        for _ in range(i[0]):
            crates[i[2]-1].insert(0, crates[i[1]-1][0])
            crates[i[1]-1].pop(0)
    answer = "*"
    for i in range(len(crates)):
        answer += crates[i][0]
    answer += "*"
    return answer
def part2(data):
    orders = [[int(y) for y in x]for x in data[1]]
    crates = data[0]
    for i in orders:
        for j in range(i[0]):
            crates[i[2]-1].insert(j, crates[i[1]-1][0])
            crates[i[1]-1].pop(0)
    answer = "*"
    for i in range(len(crates)):
        answer += crates[i][0]
    answer += "*"
    return answer
print(part1(parse_input("input.txt")))
print(part2(parse_input("input.txt")))
