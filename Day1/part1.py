import math

path = "L5, R1, R3, L4, R3, R1, L3, L2, R3, L5, L1, L2, R5, L1, R5, R1, L4, R1, R3, L4, L1, R2, R5, R3, R1, R1, L1, R1, L1, L2, L1, R2, L5, L188, L4, R1, R4, L3, R47, R1, L1, R77, R5, L2, R1, L2, R4, L5, L1, R3, R187, L4, L3, L3, R2, L3, L5, L4, L4, R1, R5, L4, L3, L3, L3, L2, L5, R1, L2, R5, L3, L4, R4, L5, R3, R4, L2, L1, L4, R1, L3, R1, R3, L2, R1, R4, R5, L3, R5, R3, L3, R4, L2, L5, L1, L1, R3, R1, L4, R3, R3, L2, R5, R4, R1, R3, L4, R3, R3, L2, L4, L5, R1, L4, L5, R4, L2, L1, L3, L3, L5, R3, L4, L3, R5, R4, R2, L4, R2, R3, L3, R4, L1, L3, R2, R1, R5, L4, L5, L5, R4, L5, L2, L4, R4, R4, R1, L3, L2, L4, R3"

north = "N"
south = "S"
east = "E"
west = "W"

class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __mul__(self, i):
        return Point(self.x * i, self.y * i)
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

directionVectors = {north: Point(0, 1), south: Point(0, -1), east: Point(1, 0), west: Point(-1, 0)}

currentDirection = north
currentPosition = Point(0, 0)

for ins in path.split(", "):
    dir = ins[0]
    nbMove = int(ins[1:])

    if currentDirection == north: currentDirection = west if dir == "L" else east
    elif currentDirection == south: currentDirection = east if dir == "L" else west
    elif currentDirection == east: currentDirection = north if dir == "L" else south
    elif currentDirection == west: currentDirection = south if dir == "L" else north

    vec = directionVectors[currentDirection] * nbMove
    currentPosition = currentPosition + vec

print (abs(currentPosition.x) + abs(currentPosition.y))