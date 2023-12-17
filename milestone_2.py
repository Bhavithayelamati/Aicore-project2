import random

def check_guess(word, guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

def ask_for_input(word):
    while True:
        guess = input("Enter a single letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            check_guess(word, guess)
            break
        else:
            print("Oops! That is not a valid input.")

def play_hangman(word_list):
    while True:
        word = random.choice(word_list)
        hidden_word = ['_' for _ in word]
        print(" ".join(hidden_word))
        ask_for_input(word)
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    favorite_fruits = ["banana", "strawberry", "apple", "kiwi", "orange"]
    word_list = favorite_fruits
    print("List of words:", word_list)

    play_hangman(word_list)
