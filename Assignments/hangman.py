# DL, Hangman
#note: this is case sensitive so we should do .lower()

# Create a list of 10 words on a separate txt file
# create another file holds qwins/loss counts
# Use split(",") on the content of the words txt document to create your list of words
# pull win and lose totals from the other txt files and save them as 2 separate variables
#build the hangman game
# save the correct word as a variable random.choice(name of list)
# number of wrong guesses
# what letters have been guessed

# function to display the hangman (needs numbers of wrong guesses)
"""_______
    |    |
    |    O
    |   /|\\
    |   / \\
    |________
"""

# function to show the letters and space (the correct word, letters that have been guessed)

# loop over the correct word
    # variable for display word (starts as an empty string)
    #check if letter has been guessed
        # than add the letter to the display word
    # if they haven't guessed it
        # add an underscore to the display word
#return the finished display word (outside of the loop)

# main game loop (while True)
# call function to show hangman
# print function call to show display word
# create variable and ask user to guess a letter
# add the letter to list of guessed letters
# check if not letter in word
    # increasse incorrect guesses
# check if display word is the same as the word
    # tell user they won
    # increase win total
    # ask if they want to play again
    # reset random word, reset wrong guess count
# check to see if they lost (if they have 6 wrong guesses)
    #tell them they lost
    # tell them what the word was
    # increases the lost count
    # ask if they want to play again
                #reset random word, reset worng guess count

                