#  out cum of day 7 usings of:
#  loops list string if/else and everything that you need to know
#  before to start oop

import random

from hangman_art import stages, logo
from hangman_words import word_list


print(logo)
chosen_word = word_list[random.randint(0, len(word_list)-1)]


display = []
word_length = len(chosen_word)
for letter in range(word_length):
    display.append("_")
print(display)


end_of_game = False
lives = len(stages)-1

while (not end_of_game):

    guess = input("enter a letter: ")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"wrong letter: {guess}, you have {lives} remaining lives")
        print(display)
        if lives == 0:
            end_of_game = True
            print("you lots")
            print(f"the word was {chosen_word}")

    if "_" not in display:
        end_of_game = True
        print("you win")
        print(f"the word is {display}")
    print(stages[lives])
