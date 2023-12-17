import random

# Step 1: Define a function called check_guess. Pass in the guess as a parameter.
def check_guess(guess, secret_word):
    # Step 2: Convert the guess into lower case.
    guess = guess.lower()
    
    # Step 3: Check if the guess is in the word.
    if guess in secret_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

# Step 1: Define a function called ask_for_input.
def ask_for_input():
    # Step 2: Move the code to check if the guess is a valid input into this function block.
    while True:
        # Step 2 (continued): Ask the user to guess a letter and assign it to a variable called guess.
        guess = input("Guess a letter: ")

        # Step 3: Check if the guess is a single alphabetical character.
        if guess.isalpha() and len(guess) == 1:
            # Step 4: If the guess passes the checks, break out of the loop.
            break
        else:
            # Step 5: If the guess does not pass the checks, print an error message.
            print("Invalid letter. Please, enter a single alphabetical character.")

    # Step 3 (continued): Outside the while loop, call the check_guess function to check if the guess is in the word.
    check_guess(guess, secret_word)

# Outside the functions, set the secret_word (replace "apple" with your actual secret word).
secret_word = "apple"

# Step 4: Outside the functions, call the ask_for_input function to test your code.
ask_for_input()
