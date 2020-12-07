import re
import string

bags = {}
with open("input.txt", "r") as file:
    for line in file:
        rule = re.split("contain", line)
        topBag = rule[0].rstrip()
        if topBag[len(topBag) - 1] != 's':
            topBag += 's'
        bags[topBag] = {}
        insideBags = re.split(r',', rule[1].strip())
        for bag in insideBags:
            num = re.search(r'\d\s', bag)
            if num:
                innerBag = bag[num.span()[1]:].translate(str.maketrans('', '', string.punctuation))
                if innerBag[len(innerBag) - 1] != 's':
                    innerBag += 's'
                bags[topBag][innerBag] = int(bag[num.span()[0]:num.span()[1]].strip())
            

# Handy Haversacks: Part 1
def containsShinyGoldBag(bags: dict, bag: dict):
    if "shiny gold bags" in bag:
        return True
    if len(bag) == 0:
        return False
    
    for b in bag:
        if containsShinyGoldBag(bags, bags[b]):
            return True
        
bagsContainingGold = 0
for bag in bags:
    if bag and containsShinyGoldBag(bags, bags[bag]):
        bagsContainingGold += 1

print("Bags containing shiny gold bags: " + str(bagsContainingGold))

# Handy Haversacks: Part 2
def countBags(bags: dict, color: dict) -> int: 
    counter = sum(bags[color].values())
    for b in bags[color]:
        counter += bags[color][b] * countBags(bags, b)
    return counter

print("Bags inside shiny gold bag: " + str(countBags(bags, "shiny gold bags")))
