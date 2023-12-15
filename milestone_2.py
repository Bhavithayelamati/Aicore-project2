import random

def validate_input(guess):
    # Check if the input is a single character and alphabetical
    if len(guess) == 1 and guess.isalpha():
        return True
    else:
        print("Oops! That is not a valid input.")
        return False

# List of favorite fruits
favorite_fruits = ["banana", "strawberry", "apple", "kiwi", "orange"]
word_list = favorite_fruits

# Print the list of words
print("List of words:", word_list)

while True:
    # Randomly choose a word
    word = random.choice(word_list)
    
    # Display a placeholder for the word (you may replace this with your actual game logic)
    hidden_word = ['_' for _ in word]
    print(" ".join(hidden_word))

    # Ask the user to guess a letter
    guess = input("Enter a single letter: ")

    # Validate the user's input
    if validate_input(guess):
        # Step 1: Check if the guess is in the word
        if guess in word:
            # Step 2: Print a message for a correct guess
            print(f"Good guess! '{guess}' is in the word.")
        else:
            # Step 3: Print a message for an incorrect guess
            print(f"Sorry, '{guess}' is not in the word. Try again.")

    # Optionally, you can add logic here to update the displayed word based on the correct guesses

    # Check if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break
