# DL, Number Guessing Game

import random

number = random.randint(1, 50)

attempts = 6
guesses = 0

print("I'm thinking of a number between 1 and 50.")
print(f"You have {attempts} tries to guess it!")

while guesses < attempts:
    guess = int(input(f"Guess #{guesses + 1}: "))

    guesses += 1

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Correct! You guessed it in {guesses} tries!")
        break

if guesses == attempts and guess != number:
    print(f"You're out of guesses! The number was {number}.")
