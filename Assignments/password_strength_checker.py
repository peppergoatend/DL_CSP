# DL, Password Strength Checker

password = input("What is your password:")
length = "Weak"
upper = False
lower = False
number = False
Symbol = False

if len(password) >= 8:
    length = True
else:
    print("At least 8 characters: {length}")

for letter in password:

    letter.islower()
    letter.isupper()
    letter.isnumeric()
    "! @ # $ % ^ & *"
