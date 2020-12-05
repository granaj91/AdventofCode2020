import math
file = open("input.txt", "r")
report = []

for num in file:
    report.append(int(num))

# Report Repair: Part 1
report.sort()
i = 0
j = len(report) - 1
while i < j:
    while(report[i] + report[j] > 2020):
        j -= 1
    if report[i] + report[j] == 2020:
        print(report[i] * report[j])
        break
    i += 1

# Report Repair: Part 2
for i in range(len(report)):
    for j in range(i, len(report)):
        for k in range(j, len(report)):
            if report[i] + report[j] + report[k] == 2020:
                print(report[i] * report[j] * report[k])
                break