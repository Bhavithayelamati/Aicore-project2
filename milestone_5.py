# milestone_5.py

import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = self.choose_random_word()
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def choose_random_word(self):
        return random.choice(self.word_list)

    def check_guess(self, guess):
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")

            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
                    self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")

            if guess.isalpha() and len(guess) == 1:
                if guess not in self.list_of_guesses:
                    self.list_of_guesses.append(guess)
                    self.check_guess(guess)
                else:
                    print("You already tried that letter!")
            else:
                print("Invalid letter. Please, enter a single alphabetical character.")

    def play_game(self):
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
    num_lives = 5
    game = Hangman(word_list, num_lives)
    game.play_game()


