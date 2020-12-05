import math

def findSeat(boardpass: str, frontHalf: int, backHalf: int) -> int:
    if len(boardpass) == 0:
        return frontHalf
    
    if boardpass[0] == 'F' or boardpass[0] == 'L':
        return findSeat(boardpass[1:], frontHalf, math.ceil((backHalf - frontHalf)/2 + frontHalf))
    else:
        return findSeat(boardpass[1:], math.ceil((backHalf - frontHalf)/2 + frontHalf), backHalf)

      

maxID = 0
boardingpassList = [0 for i in range(maxID + 1)]
with open("input.txt", "r") as file:
    for line in file:
        row = findSeat(line[:7], 0, 127)
        col = findSeat(line[7:].rstrip(), 0, 7)
        passID = row * 8 + col
        
        if passID > maxID:
           maxID = passID
        
        boardingpassList[passID] = passID

# Binary Boarding: Part 1
print("Max. boarding pass ID: " + str(maxID))

# Binary Boarding: Part 2

# Remove non-existent rows in front of plane
i = 0
while(boardingpassList[i] == 0):
    i += 1
del boardingpassList[:i]

print("My boarding pass ID: " + str(boardingpassList.index(0) + i))