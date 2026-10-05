# DL, Hangman

import random

words = []

with open("Assignments/words.txt", "r") as file:
    for line in file:
        words.append(line.strip())
        
secret_word = random.choice(words)

try:
    stats = []

    with open("Assignments/stats.txt", "r") as file:
        for line in file:
            stats.append(line.strip())

    wins = int(stats[0])
    losses = int(stats[1])

except:
    wins = 0
    losses = 0

guessed_letters = []
wrong_guesses = 0

max_wrong_guesses = 6


def show_word(secret_word, guessed_letters):
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    return display_word

print(words)