#!/usr/bin/env python3
import math
from types import coroutine
def parseInput(filename):
    with open(filename, "r") as file:
        data = [x.strip() for x in file]
        maze_positions = {}
        levelWidth = 0
        levelHeight = len(data)
        startPositions = []
        for i in range(len(data)):
            if levelWidth == 0: levelWidth = len(data[i])
            for j in range(len(data[i])):
                if data[i][j] == "S":
                    data[i] = data[i].replace("S", "a")
                    maze_positions.update({"StartPosition": [int(j),int(i)]})
                if data[i][j] == "a":
                    startPositions.append([int(j),int(i)])
                if data[i][j] == "E":
                    maze_positions.update({"EndPosition": [int(j),int(i)]})
                    data[i] = data[i].replace("E", "z")
        return data, maze_positions, (levelHeight, levelWidth), startPositions
def getNextMoves(x,y):
    return {
        "left": [x-1, y],
        "right": [x+1,y],
        "up": [x, y-1],
        "down": [x, y+1]
    }.values()
def getShortestPath(level, startCoordinate, endCoordinate, levelHeight, levelWidth) -> int:
    searchPaths = [[startCoordinate]]
    visitedCoordinates = [startCoordinate]
    while searchPaths != []:
        currentPath = searchPaths.pop(0)
        currentCoordinate = currentPath[-1]
        # print(currentCoordinate)
        currentX, currentY = currentCoordinate
        if currentCoordinate == endCoordinate:
            return len(currentPath)-1
        for nextCoordinate in getNextMoves(currentX, currentY):
            nextX, nextY = nextCoordinate
            if nextX < 0 or nextX >= levelWidth:
                continue
            if nextY < 0 or nextY >= levelHeight:
                continue
            if nextCoordinate in visitedCoordinates:
                continue
            if (ord(level[nextY][nextX]) - ord(level[currentY][currentX])  > 1):
                continue
            searchPaths.append(currentPath + [nextCoordinate])
            visitedCoordinates += [nextCoordinate]
    return 0
input = parseInput("input.txt")
# shortestPath = getShortestPath(input[0], input[1]["StartPosition"], input[1]["EndPosition"], input[2][0], input[2][1])
# print(shortestPath-1)
endPosition = input[1]["EndPosition"]
min_diff = 5000
minStartPositions = list()
for i in input[-1]:
    diff = math.dist(endPosition,i)
    if diff < min_diff:
        minStartPositions.append(([i[0], i[1], diff]))
minStartPositions = sorted(minStartPositions, key=lambda x: x[2])
paths = list()
for startPosition in minStartPositions:
    path = getShortestPath(input[0], startPosition[0:2], input[1]["EndPosition"], input[2][0], input[2][1])
    if path != 0:
        paths.append(path)
        print(min(paths))
print(min(paths))
