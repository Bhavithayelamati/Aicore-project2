favorite_fruits = [ "banana",  "strawberry", "apple" ,"kiwi","orange",]
word_list = favorite_fruits
print(word_list)
import random
word = random.choice(word_list)
print(word)
guess = input("Enter a single letter: ")
# Check if the input is a single character and alphabetical
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
