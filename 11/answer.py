import numpy as np

divisors = [2, 17, 7, 11, 19, 5, 13, 3]
divisors = np.product(divisors)

class Monkey:
    def __init__(self, data: list[str], p: int) -> None:
        self.items = list()
        data = data[1:]
        items = [x.split(",") for x in data[0][data[0].find(":") :].split(" ")]
        items = [item for sublist in items for item in sublist]
        for i in items:
            if i == ":" or i == "":
                pass
            else:
                self.items.append(np.uint64(i))
        self.operation = data[1][data[1].find("old") :].split()[1:]
        if self.operation[1] != "old":
            self.operation[1] = int(self.operation[1])
        else:
            self.operation[1] = 0
        self.divisible = [int(data[2].split()[-1])]
        self.divisible.append(int(data[3].split()[-1]))
        self.divisible.append(int(data[4].split()[-1]))
        self.items_inspected = 0
        self.p = p
    def AddItem(self, itemToAdd) -> None:
        self.items.append(itemToAdd)

    def RemoveItem(self, itemIDToRemove) -> None:
        del self.items[itemIDToRemove]

    def GetStressLevel(self, itemID) -> None:
        self.items_inspected += 1
        if self.operation[1] == 0:
            if self.operation[0] == "+":
                self.items[itemID] += self.items[itemID]
            else:
                self.items[itemID] *= self.items[itemID]
        elif self.operation[1] != 0: 
            if self.operation[0] == "+":
                self.items[itemID] += self.operation[1]
            else:
                self.items[itemID] *= self.operation[1]
        if self.p == True:
            self.MonkeyGetsBored(itemID=itemID)
        self.ReduceBigNumbers(itemID=itemID)

    def MonkeyGetsBored(self, itemID) -> None:
        self.items[itemID] //= 3

    def ReduceBigNumbers(self, itemID) -> None:
        self.items[itemID] %= divisors

    def GetNextMonkey(self, itemID) -> bool:
        if self.items[itemID] % self.divisible[0] == 0:
            return self.divisible[1]
        else:
            return self.divisible[2]

    def __repr__(self) -> str:
        return f"items: {self.items}, inspected: {self.items_inspected}"


def parseInput(filename):
    with open(filename, "r") as f:
        data = f.read().strip().split("\n\n")
        data = [x.strip().split("\n") for x in data]
        monkeysP1 = list()
        monkeysP2 = list()
        for i in data:
            monkeysP1.append(Monkey(data=i.copy(), p=True))
            monkeysP2.append(Monkey(data=i.copy(), p=False))
        return monkeysP1, monkeysP2


def part1(monkeys: list[Monkey], rounds):
    for _ in range(rounds):
        for index in range(len(monkeys)):
            currentMonkey = monkeys[index]
            while len(currentMonkey.items) > 0:
                currentMonkey.GetStressLevel(itemID=0)
                nextMonkey = currentMonkey.GetNextMonkey(itemID=0)
                monkeys[nextMonkey].AddItem(itemToAdd=currentMonkey.items[0])
                currentMonkey.RemoveItem(itemIDToRemove=0)
    return monkeys


def MonkeyBussinessLevel(monkeysAfterRounds):
    inspected = list()
    for i in monkeysAfterRounds:
        inspected.append(i.items_inspected)
    inspected = sorted(inspected)[::-1]
    return inspected[0] * inspected[1]


input = parseInput("input.txt")
print(MonkeyBussinessLevel(part1(input[0], 20)))
print(MonkeyBussinessLevel(part1(input[1], 10000)))
