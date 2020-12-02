import re
file = open("input.txt", "r")
lines = file.readlines()
file.close()
validPasswords = 0

# Password Philosophy: Part 1
for line in lines:
    rule = re.split(r'-|\s', line)
    char = rule[2].replace(':', '')
    minFreq = int(rule[0])
    maxFreq = int(rule[1])
    password = rule[3]
    count = 0
    for c in password:
        if c == char:
            count += 1
    if count >=  minFreq and count <= maxFreq:
        validPasswords += 1

print(validPasswords)

# Password Philosophy: Part 2
validPasswords = 0
for line in lines:
    rule = re.split(r'-|\s', line)
    char = rule[2].replace(':', '')
    firstLoc = int(rule[0]) - 1
    secondLoc = int(rule[1]) - 1
    password = rule[3]

    if ((password[firstLoc] == char and password[secondLoc] != char) or 
    (password[firstLoc] != char and password[secondLoc] == char)):
        validPasswords += 1
 
print(validPasswords)