import random

def check_guess(word, guess):
    # Step 2: Convert the guess into lower case
    guess = guess.lower()

    # Step 3: Check if the guess is in the word
    if guess in word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

def ask_for_input():
    while True:
        # Step 2: Move the code for input validation into ask_for_input
        guess = input("Enter a single letter: ")

        # Validate the user's input
        if len(guess) == 1 and guess.isalpha():
            # Step 3: Call check_guess to check if the guess is in the word
            check_guess(word, guess)
            break
        else:
            print("Oops! That is not a valid input.")

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

    # Step 4: Call ask_for_input outside the while loop to test the code
    ask_for_input()

    # Check if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break
