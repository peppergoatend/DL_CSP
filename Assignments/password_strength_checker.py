# DL, Password Strength Checker

password = input("What is your password: ")

length = len(password) >= 8

uppercase = False
lowercase = False
number = False
symbol = False

symbols = "!@#$%^&?*"

for letter in password:
    if letter.isupper():
        uppercase = True
    if letter.islower():
        lowercase = True
    if letter.isnumeric():
        number = True
    if letter in symbols:
        symbol = True

rules_met = 0

if length:
    rules_met = rules_met + 1

if uppercase:
    rules_met = rules_met + 1

if lowercase:
    rules_met = rules_met + 1

if number:
    rules_met = rules_met + 1

if symbol:
    rules_met = rules_met + 1

if rules_met == 5:
    strength = "Strong"
elif rules_met >= 3:
    strength = "Medium"
else:
    strength = "Weak"


print(f"At least 8 characters: {length}")
print(f"Has an uppercase letter: {uppercase}")
print(f"Has a lowercase letter: {lowercase}")
print(f"Has a number: {number}")
print(f"Has a symbol: {symbol}")
print(f"Your password strength is: {strength}")

if strength != "Strong":
    print("To make it Strong, add:")

    if not length:
        print("at least 8 characters")

    if not uppercase:
        print("an uppercase letter")

    if not lowercase:
        print("a lowercase letter")

    if not number:
        print("a number")

    if not symbol:
        print("a symbol")
