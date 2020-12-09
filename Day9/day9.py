preamble = list()
MAX_PREAMBLE = 25
with open("input.txt") as file:
    for line in file:
        preamble.append(int(line.rstrip()))

def checkForSum(pre: list(), val: int) -> bool:
    for i, x in enumerate(pre):
        if (val - x) in pre[i:]:
            return True
    return False

def findContiguousSum(pre: list(), val: int) -> list():
    contig = list()
    total = 0
    for x in pre:
        total += x
        contig.append(x)
        if total == val:
            return contig
        elif total > val:
            return None

# Encoding Error: Part 1
noSum = 0
for i in range(MAX_PREAMBLE, len(preamble)):
    if not checkForSum(preamble[i - MAX_PREAMBLE:i], preamble[i]):
        noSum = preamble[i]
        print(preamble[i])
        break

print("No sum in preamble for: " + str(noSum))


# Encoding Error: Part 2
contigSum = list()
for i in range(len(preamble)):
    if preamble[i] != noSum:
        contigSum = findContiguousSum(preamble[i:], noSum)
    if contigSum:
        break
    
print("Sum of min and max values in contiguous array: " + str(min(contigSum) + max(contigSum)))