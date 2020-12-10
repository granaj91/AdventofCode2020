import copy
import math
adaptors = list()
with open("test_input.txt") as file:
    for line in file:
        adaptors.append(int(line.rstrip()))

list.sort(adaptors)

OUTLET = 0
BUILTIN = adaptors[len(adaptors) - 1] + 3
adaptors.insert(0, OUTLET)
adaptors.append(BUILTIN)

# Adaptor Array: Part 1
diffThree = 0
diffOne = 0
for i in range(1, len(adaptors)):
    diff = adaptors[i] - adaptors[i - 1]
    if diff == 1:
        diffOne += 1
    elif diff == 3:
        diffThree += 1

print("Diff of one: " + str(diffOne) + ", Diff of three: " + str(diffThree))
print(str(diffOne * diffThree))