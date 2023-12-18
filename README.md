# Hangman Game

## Table of Contents
- [Project Title](#hangman-game)
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Milestones](#milestones)
  - [Milestone 1: Define the List of Possible Words](#milestone-1-define-the-list-of-possible-words)
  - [Milestone 2: Choose a Random Word from the List](#milestone-2-choose-a-random-word-from-the-list)
  - [Milestone 3: Ask the User for Input and Validate](#milestone-3-ask-the-user-for-input-and-validate)
  - [Milestone 4: Check if the Guessed Letter is in the Word](#milestone-4-check-if-the-guessed-letter-is-in-the-word)
  - [Milestone 5: Implement Hangman Class and Run the Game](#milestone-5-implement-hangman-class-and-run-the-game)
- [File Structure](#file-structure)
- [License](#license)

## Description
Hangman is a classic game where a player thinks of a word, and another player tries to guess it within a certain number of attempts. This implementation is a computerized version where the computer selects a word, and the user tries to guess it. The aim of the project is to provide an entertaining and interactive experience while practicing basic Python concepts.

## Installation
To set up the Hangman game on your local machine:

1. Ensure you have Python installed.
2. Download or clone the repository to your preferred directory.
3. Open a terminal or command prompt.
4. Navigate to the project directory.
5. Run the `milestone_5.py` file to initiate the Hangman game.

## Milestones

### Milestone 1: Define the List of Possible Words
- Create a list containing the names of your 5 favorite fruits.
- Assign this list to a variable called `word_list`.
- Print out the newly created list to the standard output (screen).

### Milestone 2: Choose a Random Word from the List
- Import the `random` module.
- Use the `random.choice` method to pick a word from the `word_list`.
- Assign the randomly generated word to a variable called `word`.
- Print out the chosen word.

### Milestone 3: Ask the User for Input and Validate
- Create a while loop for continuous user input.
- Ask the user to guess a letter and assign it to a variable called `guess`.
- Check if the guess is a single alphabetical character.
- If the guess is valid, break out of the loop; otherwise, print an error message.

### Milestone 4: Check if the Guessed Letter is in the Word
- Create an `if` statement to check if the guessed letter is in the word.
- Print a message indicating whether the guess is correct or not.

### Milestone 5: Implement Hangman Class and Run the Game
- Create a Hangman class with an `__init__` method to initialize game attributes.
- Define a `check_guess` method to handle checking if the guess is in the word.
- Define an `ask_for_input` method to manage user input and call the `check_guess` method.
- Implement a `play_game` function that orchestrates the game logic.
- Run the game using the `play_game` function.

## File Structure
Hangman/
│
├── milestone_5.py
│
└── README.md
