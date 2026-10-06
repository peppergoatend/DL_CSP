# DL, Hangman

import random

with open("Assignments/words.txt", "r") as file:
    content = file.read()
    words = content.split(",")

secret_word = random.choice(words)

try:
    with open("Assignments/stats.txt", "r") as file:
        content = file.read()
        stats = content.split(",")

    wins = int(stats[0])
    losses = int(stats[1])

except:
    wins = 0
    losses = 0

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6


def show_hangman(wrong_guesses):
    if wrong_guesses == 0:
        print("""
 _______
 |     |
 |
 |
 |
 |________
""")
    elif wrong_guesses == 1:
        print("""
 _______
 |     |
 |     O
 |
 |
 |________
""")
    elif wrong_guesses == 2:
        print("""
 _______
 |     |
 |     O
 |     |
 |
 |________
""")
    elif wrong_guesses == 3:
        print("""
 _______
 |     |
 |     O
 |    /|
 |
 |________
""")
    elif wrong_guesses == 4:
        print("""
 _______
 |     |
 |     O
 |    /|\\
 |
 |________
""")
    elif wrong_guesses == 5:
        print("""
 _______
 |     |
 |     O
 |    /|\\
 |    /
 |________
""")
    else:
        print("""
 _______
 |     |
 |     O
 |    /|\\
 |    / \\
 |________
""")
#me after:

def show_word(secret_word, guessed_letters):
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word = display_word + letter
        else:
            display_word = display_word + "_"

    return display_word
    
#I have a headache

while True:
    show_hangman(wrong_guesses)

    print(show_word(secret_word, guessed_letters))

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
    else:
        guessed_letters.append(guess)

        if guess not in secret_word:
            wrong_guesses = wrong_guesses + 1
            print("Wrong guess!")

        if show_word(secret_word, guessed_letters) == secret_word:
            print("You won!")
            wins = wins + 1

            play_again = input("Do you want to play again? ").lower()

            if play_again == "yes":
                secret_word = random.choice(words)
                guessed_letters = []
                wrong_guesses = 0
            else:
                break

        if wrong_guesses == max_wrong_guesses:
            show_hangman(wrong_guesses)
            print("You lost!")
            print("The word was:", secret_word)
            losses = losses + 1

            play_again = input("Do you want to play again? ").lower()

            if play_again == "yes":
                secret_word = random.choice(words)
                guessed_letters = []
                wrong_guesses = 0
            else:
                break
#that was so painful to make

with open("Assignments/stats.txt", "w") as file:
    file.write(str(wins) + "," + str(losses))

print("All-time wins:", wins)
print("All-time losses:", losses)
