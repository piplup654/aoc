class Rucksack:
    def __init__(self, items):
        self.items = items
        self.first_compartment = list()
        self.second_compartment = list()
        self.common_item = ""
    def splitRucksackToCompartments(self):
        self.first_compartment = self.items[:len(self.items)//2]
        self.second_compartment = self.items[len(self.items)//2:]
    def findCommonItem(self):
        for i in self.first_compartment:
            for j in self.second_compartment:
                if i == j:
                    self.common_item = i
lowercase_val = dict()
uppercase_val = dict()
for i in range(0,26):
    lowercase_val[chr(ord("a")+i)] = i+1
    uppercase_val[chr(ord("A")+i)] = i+27
def partA(file):
    final_sum = 0
    for line in file.readlines():
        rucksack = Rucksack(line)
        rucksack.splitRucksackToCompartments()
        rucksack.findCommonItem()
        # print(rucksack.first_compartment, rucksack.second_compartment, rucksack.common_item)
        if rucksack.common_item.islower():
            final_sum += lowercase_val[rucksack.common_item]
        else:
            final_sum += uppercase_val[rucksack.common_item]
    return final_sum
def partB(data):
    final_sum = 0
    excluded = list()
    print(data[::3])
    for z in data[::3]:
        c3 = data[data.index(z)+2]
        c2 = data[data.index(z)+1]
        c1 = z
        excluded.clear()
        for x in c1:
            for y in c2:
                for d in c3:
                    if x == y == d:
                        if x not in excluded:
                            if x.islower():
                                final_sum += lowercase_val[x]
                                excluded.append(x)
                                break
                            else:
                                final_sum += uppercase_val[x]
                                excluded.append(x)
                                break
    return final_sum
with open("input.txt", "r") as file:
    # partA(file)
    print(partB([x.strip() for x in file]))