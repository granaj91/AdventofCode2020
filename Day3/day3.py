tobogganMap = []
with open("input.txt", "r") as file:
    for line in file:
        tobogganMap.append(line.rstrip())

trees = 0
j = 3
for i in range(1, len(tobogganMap)):
    if(j >= len(tobogganMap[i])):
        j = j - (len(tobogganMap[i]))
    if(j < len(tobogganMap[i]) and tobogganMap[i][j] == '#'):
        trees += 1
    j += 3
    
print(trees)