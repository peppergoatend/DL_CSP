# DL, Loops Notes
import random

# code that will repeat over and over again
count = 1

while count <= 10:
    print(count)
    count += 1

goose = random.randint(1,11)
ducks = 1

while True:
     print("duck")
     if ducks == goose:
        break
     ducks += 1
print("GOOSE!!")



siblings = ["Byron", "Mochi"]

print(siblings[1])
print(siblings)
# add to the list
item = input("What needs to be added to the list:")
siblings.append("Novie")
siblings.insert(2, "Nori")
# remove from list
print(siblings)
print(siblings.pop(0))
print(siblings)

# For Loops
for number in range(1,11,2): # 1 is your start point, 11 is your end point, 2 is our incrementor
    # Keyword for "for loop" is "for"
    print(number)

for sibling in siblings:
    print(sibling + " " + "Le")