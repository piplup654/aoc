import time
from dataclasses import dataclass
from functools import reduce
def parse_input(filename):
    with open(filename, "r") as file:
        data = [[e.split(" ") for e in d] for d in [[z.strip() for z in y if z != ""] for y in [x.split("\n") for x in file.read().split("$")]] if d != list()]
        return data
class Folder:
    def __init__(self, name: str, parent):
        self.name = name
        self.parent = parent
        self.subfolders, self.files, self.output = [],[],[]
    def AddSubFolder(self, name: str):
        if name not in self.get_sub_names():
            subFolder = Folder(name, self)
            self.subfolders.append(subFolder)
    def AddFile(self, name: str, size: int):
        if name not in self.get_file_names():
            file = File(name, size, self)
            self.files.append(file)
    def getSubFolder(self, name: str):
        self.AddSubFolder(name)
        for j in self.subfolders:
            if name == j.name:
                return j
    def getParent(self):
        return self.parent
    def get_sub_names(self):
        return [n.name for n in self.subfolders]
    def get_file_names(self):
        return [n.name for n in self.files]
    def getSize(self):
        temp_size = 0
        for file in self.files:
            temp_size += file.size
        for subFolder in self.subfolders:
            temp_size += subFolder.getSize()
        return temp_size
@dataclass
class File:
    name: str
    size: int
    parent: Folder
def commands(data):
    root = Folder("/", None)
    current_folder = root
    for i in data:
        match i[0][0]:
            case "cd":
                if i[0][1] == "..":
                    current_folder = current_folder.parent
                if i[0][1] == "/":
                    current_folder = root
                if i[0][1] != "..":
                    current_folder = current_folder.getSubFolder(i[0][1])
            case "ls":
                for j in i[1:]:
                    if j[0] == "dir":
                        current_folder.AddSubFolder(j[1])
                    else:
                        current_folder.AddFile(j[1], int(j[0]))
    while current_folder.parent != None: current_folder = current_folder.parent
    return current_folder
time1 = time.time()
pam = commands(parse_input("input.txt"))
ans_list = list()
def getSum(folder: Folder):
    for sub in folder.subfolders:
        ans_list.append(sub.getSize())
        getSum(sub)
getSum(pam)
# part1
print(sum([v for v in ans_list if v <= 100000]))
# part2
unused = 70000000 - ans_list[0]
print(min(filter(lambda x: x + unused >= 30000000, ans_list)))
print(time.time()-time1)