file = open("input.txt", "r")
report = []

for num in file:
    report.append(int(num))

# Report Repair: Part 1
for i in range(len(report)):
    for j in range(i, len(report)):
        if report[i] + report[j] == 2020:
            print(report[i] * report[j])
            break

# Report Repair: Part 2
for i in range(len(report)):
    for j in range(i, len(report)):
        for k in range(j, len(report)):
            if report[i] + report[j] + report[k] == 2020:
                print(report[i] * report[j] * report[k])
                break