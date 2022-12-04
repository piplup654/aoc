with open("input.txt", "r") as file:
    data = map(lambda x: list(map(lambda y: y.split("-"), x.strip().split(","))), file)
    counter1 = 0
    counter2 = 0
    for i in data:
        elf1 = set(map(lambda x: int(x), range(int(i[0][0]), int(i[0][1])+1)))
        elf2 = set(map(lambda x: int(x), range(int(i[1][0]), int(i[1][1])+1)))
        if elf1.issubset(elf2) or elf2.issubset(elf1):
            counter1 += 1
        if not elf1.isdisjoint(elf2):
            counter2 += 1
    print(counter1, counter2)