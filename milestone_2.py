import random

def choose_random_word(word_list):
    return random.choice(word_list)

def get_user_guess():
    return input("Enter a single letter: ")

def validate_guess(guess):
    if len(guess) == 1 and guess.isalpha():
        print("Good guess!")
    else:
        print("Oops! That is not a valid input.")

# Task 1: Define the list of possible words
favorite_fruits = ["banana", "strawberry", "apple", "kiwi", "orange"]

# Assign this list to a variable called word_list
word_list = favorite_fruits

# Print out the newly created list to the standard output (screen)
print(word_list)

# Task 2: Choose a random word from the list
word = choose_random_word(word_list)

# Assign the randomly generated word to a variable called word
print(word)

# Task 3: Ask the user for an input
# Using the input function, ask the user to enter a single letter
# Assign the input to a variable called guess
guess = get_user_guess()

# Task 4: Check that the input is a single character
validate_guess(guess)
