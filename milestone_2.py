# Ask the user to enter a single letter
guess = input("Enter a single letter: ")

# Check if the input is a single character and alphabetical
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
