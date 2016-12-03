path = "L5, R1, R3, L4, R3, R1, L3, L2, R3, L5, L1, L2, R5, L1, R5, R1, L4, R1, R3, L4, L1, R2, R5, R3, R1, R1, L1, R1, L1, L2, L1, R2, L5, L188, L4, R1, R4, L3, R47, R1, L1, R77, R5, L2, R1, L2, R4, L5, L1, R3, R187, L4, L3, L3, R2, L3, L5, L4, L4, R1, R5, L4, L3, L3, L3, L2, L5, R1, L2, R5, L3, L4, R4, L5, R3, R4, L2, L1, L4, R1, L3, R1, R3, L2, R1, R4, R5, L3, R5, R3, L3, R4, L2, L5, L1, L1, R3, R1, L4, R3, R3, L2, R5, R4, R1, R3, L4, R3, R3, L2, L4, L5, R1, L4, L5, R4, L2, L1, L3, L3, L5, R3, L4, L3, R5, R4, R2, L4, R2, R3, L3, R4, L1, L3, R2, R1, R5, L4, L5, L5, R4, L5, L2, L4, R4, R4, R1, L3, L2, L4, R3"

NORTH = "N"
SOUTH = "S"
EAST = "E"
WEST = "W"

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
    def toTuple(self):
        return (self.x, self.y)

directionVectors = {NORTH: Point(0, 1), SOUTH: Point(0, -1), EAST: Point(1, 0), WEST: Point(-1, 0)}

def followPath(pathEntries):
    pos = Point(0, 0)
    currentDirection = NORTH
    visited = {(pos.x, pos.y): 1}

    for ins in pathEntries:
        dir = ins[0]
        nbMove = int(ins[1:])

        if currentDirection == NORTH: currentDirection = WEST if dir == "L" else EAST
        elif currentDirection == SOUTH: currentDirection = EAST if dir == "L" else WEST
        elif currentDirection == EAST: currentDirection = NORTH if dir == "L" else SOUTH
        elif currentDirection == WEST: currentDirection = SOUTH if dir == "L" else NORTH

        for i in range(0, nbMove):        
            pos += directionVectors[currentDirection]
            visited[pos.toTuple()] = visited.get(pos.toTuple(), 0) + 1
            if visited[pos.toTuple()] == 2:
                return pos
    return pos

pos = followPath(path.split(", "))

print (abs(pos.x) + abs(pos.y))