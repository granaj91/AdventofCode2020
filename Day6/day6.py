
# Custom Customs: Part 1
answers = set()
total = 0
with open("input.txt", "r") as file:
    for line in file:
        if line != '\n':
            for a in line.rstrip():
                answers.add(a)
        else:
            total += len(answers)
            answers.clear()
total += len(answers)
print("Yes total: " + str(total))

# Custom Customs: Part 2
answers = dict()
groupSize = 0
total = 0
with open("input.txt", "r") as file:
    for line in file:
        if line != '\n':
            groupSize += 1
            for a in line.rstrip():
                if a not in answers:
                    answers[a] = 0
                answers[a] += 1
        else:
            for a in answers:
                if answers[a] == groupSize:
                    total += 1
            groupSize = 0
            answers.clear()

for a in answers:
    if answers[a] == groupSize:
        total += 1
print("Collective yes total: " + str(total))