
def rotateShip(current: chr, deg: int) -> chr:
    compass = {'N': 0, 'S': 180, 'E':90, 'W': 270}
    new = (compass[current] + deg) % 360
    switch = {
        0: 'N',
        90: 'E',
        180: 'S',
        270: 'W'
    }
    return switch.get(abs(new))

def rotateShipWaypoint(x: int, y: int, deg: int) -> tuple():
    for i in range(0, abs(deg), 90):
        if deg > 0:
            temp = 0 - x
            x = y
            y = temp
        else:
            temp = 0 - y
            y = x
            x = temp
    return (x, y)
    
def updateCoordinates(direction: chr, units: int) -> tuple():
    switch = {
        'N': (0, units),
        'S': (0, 0 - units),
        'E': (units, 0),
        'W': (0 - units, 0)
    }
    return switch.get(direction)

def getManhattanDistance() -> int:
    return abs(x) + abs(y)

# Rain Risk: Part 1
x = 0
y = 0
facing = 'E'
with open("input.txt") as file:
    for line in file:
        direction = line[0]
        val = int(line[1:])
        if direction == 'F':
            newX, newY = updateCoordinates(facing, val)
            x += newX
            y += newY
        elif direction == 'R':
            facing = rotateShip(facing, val)
        elif direction == 'L':
            facing = rotateShip(facing, val * -1)
        else:
            newX, newY = updateCoordinates(direction, val)
            x += newX
            y += newY 
print("Part 1: " + str(getManhattanDistance()))

# Rain Risk: Part 2
x = 0
y = 0
wx = 10
wy = 1
with open("input.txt") as file:
    for line in file:
        direction = line[0]
        val = int(line[1:])
        if direction == 'F':
            x += val * wx
            y += val * wy
        elif direction == 'R':
            wx, wy = rotateShipWaypoint(wx, wy, val)
        elif direction == 'L':
            wx, wy = rotateShipWaypoint(wx, wy, val * -1)
        else:
            newX, newY = updateCoordinates(direction, val)
            wx += newX
            wy += newY
print("Part 2: " + str(getManhattanDistance()))