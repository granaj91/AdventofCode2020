tobogganMap = []
with open("input.txt", "r") as file:
    for line in file:
        tobogganMap.append(line.rstrip())


def countTrees(right: int, down: int) -> int:
    trees = 0
    j = right
    for i in range(down, len(tobogganMap), down):
        if(j >= len(tobogganMap[i])):
            j = j - (len(tobogganMap[i]))
        if(j < len(tobogganMap[i]) and tobogganMap[i][j] == '#'):
            trees += 1
        j += right
    
    return trees

# Toboggan Trajectory: Part 1
print(countTrees(3,1))

# Toboggan Trajectory: Part 2
print(str(countTrees(1,1) * countTrees(3,1) * countTrees(5,1) * countTrees(7,1) * countTrees(1,2)))