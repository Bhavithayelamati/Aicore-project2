import random

def choose_random_word(word_list):
    return random.choice(word_list)

def check_guess(guess, secret_word):
    guess = guess.lower()
    if guess in secret_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input(secret_word):
    while True:
        guess = input("Guess a letter: ")
        if guess.isalpha() and len(guess) == 1:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess, secret_word)

def main():
    # Task 1: Define the list of possible words
    favorite_fruits = ["banana", "strawberry", "apple", "kiwi", "orange"]

    # Assign this list to a variable called word_list
    word_list = favorite_fruits

    # Print out the newly created list to the standard output (screen)
    print(word_list)

    # Task 2: Choose a random word from the list
    secret_word = choose_random_word(word_list)

    # Assign the randomly generated word to a variable called word
    print(secret_word)

    # Task 3: Ask the user for an input and check continuously
    while True:
        ask_for_input(secret_word)

if __name__ == "__main__":
    main()
