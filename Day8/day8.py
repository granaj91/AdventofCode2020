corruptInstrs = list()
with open("input.txt") as file:
    for line in file:
        corruptInstrs.append([line.rstrip(), False])

def getValue(stringVal: str):
    val = int(stringVal[1:])
    if stringVal[0] == '-':
        val = 0 - val
    return val

def accumulate(instructions: list()) -> tuple():
    acc = 0
    i = 0
    while i >= 0 and i < len(instructions):
        num = 1
        if not instructions[i][1]:
            instructions[i][1] = True
            instr = instructions[i][0].split(" ")
            if instr[0] == "acc":
                acc += getValue(instr[1])
            if instr[0] == "jmp":
                num = getValue(instr[1])
        else:
            break
        i += num
    if i >= len(instructions):
        return (True, acc)
    return (False, acc)

def resetVisitedInstructions(instructions: list()):
    for instr in instructions:
        instr[1] = False

# Handheld Halting: Part 1
_, acc = accumulate(corruptInstrs)
print("Accumulator before second execution of instruction: " + str(acc))

# Handheld Halting: Part 2
acc = 0
resetVisitedInstructions(corruptInstrs)
for instruction in corruptInstrs:
    originalInstr = instruction[0]
    instr = instruction[0].split(" ")
    if instr[0] != "acc":
        if instr[0] == "jmp":
            instruction[0] = "nop " + instr[1]
        elif instr[0] == "nop":
            instruction[0] = "jmp " + instr[1]

        finished, acc = accumulate(corruptInstrs)
        if finished:
            break
        instruction[0] = originalInstr
        resetVisitedInstructions(corruptInstrs)
        
print("Accumulator after program termination: " + str(acc))