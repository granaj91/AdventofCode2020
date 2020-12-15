import copy
seatGrid = list()
with open("input.txt") as file:
    for line in file:
        seatGrid.append(line.rstrip())

def insideBounds(x, y, maxX, maxY):
    return x >= 0 and x < maxX and y >= 0 and y < maxY

def findOccuppied(i, j, grid, direction, adj):
    found = False
    a = direction[1] + i
    b = direction[0] + j
    while insideBounds(b, a, len(grid[i]), len(grid)):
        if grid[a][b] == '#':
            return 1
        if adj or grid[a][b] == 'L':
            return 0
        a += direction[1]
        b += direction[0]
    return 0


def countOccupied(i, j, grid, adj):
    count = 0 
    count += findOccuppied(i, j, grid, (0, 1), adj) # N
    count += findOccuppied(i, j, grid, (1, 1), adj) # NE
    count += findOccuppied(i, j, grid, (1, 0), adj) # E
    count += findOccuppied(i, j, grid, (1, -1), adj) # SE
    count += findOccuppied(i, j, grid, (0, -1), adj) # S
    count += findOccuppied(i, j, grid, (-1, -1), adj) # SW
    count += findOccuppied(i, j, grid, (-1, 0), adj) # W
    count += findOccuppied(i, j, grid, (-1, 1), adj) # NW

    return count

def fillSeats(grid, adjacent, maxOccupied):
    hasChanged = True
    while hasChanged:
        filledSeats = [['' for _ in grid[0]] for _ in grid]
        hasChanged = False
        for i in range(len(grid)):
            for j, seat in enumerate(grid[i]):
                if grid[i][j] == 'L' and countOccupied(i, j, grid, adjacent) == 0:
                        filledSeats[i][j] = '#'
                        hasChanged = True
                elif grid[i][j] == '#' and countOccupied(i, j, grid, adjacent) >= maxOccupied:
                    filledSeats[i][j] = 'L'
                    hasChanged = True
                else:
                    filledSeats[i][j] = grid[i][j]
        grid = copy.deepcopy(filledSeats)

    return grid

def countTotalOccupied(grid):
    count = 0
    for i in range(len(grid)):
        for _, seat in enumerate(grid[i]):
            if seat == '#':
                count += 1
    return count

# Seating System: Part 1
newGrid = fillSeats(seatGrid, True, 4)
totalOccupied = countTotalOccupied(newGrid)
print(totalOccupied)

# Seating System: Part 2
newGrid = fillSeats(seatGrid, False, 5)
totalOccupied = countTotalOccupied(newGrid)
print(totalOccupied)