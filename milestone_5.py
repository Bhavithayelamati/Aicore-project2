# milestone_5.py

import random


class Hangman:
    def __init__(self, word_list, num_lives=5):
        """
        Initialize the Hangman game.

        Parameters:
        - word_list: List of words to choose from.
        - num_lives: Number of lives the player starts with.
        """
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = self.choose_random_word()
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def choose_random_word(self):
        """
        Choose a random word from the word list.

        Returns:
        - Randomly chosen word.
        """
        return random.choice(self.word_list)

    def check_guess(self, guess):
        """
        Check if the guessed letter is in the word.

        Parameters:
        - guess: The letter guessed by the player.
        """
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")

            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
                    self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """
        Ask the player to guess a letter and validate the input.
        """
        while True:
            guess = input("Guess a letter: ")

            if guess.isalpha() and len(guess) == 1:
                if guess not in self.list_of_guesses:
                    self.list_of_guesses.append(guess)
                    self.check_guess(guess)
                    break
                else:
                    print("You already tried that letter!")
            else:
                print("Invalid letter. Please, enter a single alphabetical character.")

    def play_game(self):
        """
        Play the Hangman game until the player wins or loses.
        """
        while True:
            if self.num_lives == 0:
                print("You lost!")
                break
            elif self.num_letters > 0:
                self.ask_for_input()
            else:
                print("Congratulations. You won the game!")
                break


def play_game(word_list):
    """
    Start the Hangman game with the given word list.

    Parameters:
    - word_list: List of words for the game.
    """
    num_lives = 5
    game = Hangman(word_list, num_lives)
    game.play_game()


if __name__ == "__main__":
    word_list = ['apple', 'banana']
    play_game(word_list)
