import re

file = open("input.txt", "r")
lines = file.readlines()
file.close()

passports = {}
passport = ""
for i in range(len(lines)):
    if i+1 >= len(lines) and lines[i] != "\n":
        passport += " " + lines[i].rstrip()
    if lines[i] == "\n" or i+1 >= len(lines):
        passports[passport] = {}
        for field in re.split(r'\s', passport): 
            fld = field.split(":")
            if fld[0] != "":
                if fld[0] not in passports[passport]:
                    passports[passport][fld[0]] = fld[1]
        passport = ""  
    else:
        passport += " " + lines[i].rstrip()


def isValid(passport):
    validFields = ["iyr", "hgt", "ecl", "pid", "eyr", "hcl", "byr"]
    if all(field in passport for field in validFields):
        if not (re.search(r'^[0-9]{4}$', passport["byr"]) and (1920 <=int(passport["byr"]) <= 2002)):
            return False
        if not (re.search(r'^[0-9]{4}$', passport["iyr"]) and (2010 <= int(passport["iyr"]) <= 2020)):
            return False
        if not (re.search(r'^[0-9]{4}$', passport["eyr"]) and (2020 <= int(passport["eyr"]) <= 2030)):
            return False
        if not re.search(r'^[0-9]+(cm|in)$', passport["hgt"]):
            return False
        if re.search(r'^[0-9]+(cm|in)$', passport["hgt"]):
            if "cm" in passport["hgt"]:
                num = passport["hgt"].replace("cm", "")
                if not int(num) >= 150 and int(num) <= 193:
                    return False
            elif "in" in passport["hgt"]:
                num = passport["hgt"].replace("in", "")
                if not int(num) >= 59 and int(num) <= 76:
                    return False
        if not re.search(r'^#([0-9]|[a-f]){6}$', passport["hcl"]):
            return False
        if not re.search(r'^(amb|blu|brn|gry|grn|hzl|oth)$', passport["ecl"]):
            return False
        if not re.search(r'^[0-9]{9}$', passport["pid"]):
            return False
    else:
        return False
    
    return True

# Passport Processing: Part 1
valid = 0
for passport in passports:
    validFields = ["iyr", "hgt", "ecl", "pid", "eyr", "hcl", "byr"]
    if all(field in passport for field in validFields):
        valid += 1

print("Valid passports: " + str(valid))

# Passport Processing: Part 2
valid = 0
for passport in passports:
    if isValid(passports[passport]):
        valid += 1

print("Valid passports: " + str(valid))
