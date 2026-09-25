# DL, Number Guessing game
import random

print("I'm thinking of a number between 1 and 100. You have 6 tries to guess it!")

guess = 1

for guess in range(1,11):
    print(guess)

for number in guess:
    print(guess+ " " + "1")
    if number == guess:
        break

number = random.randint(1,11)
