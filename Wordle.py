# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, N_ROWS, WordleGWindow, WordleSquare

def wordle():
    # selects a random word from the wordle dictionary
    rand_word = random.choice(FIVE_LETTER_WORDS)
    print(rand_word)

    def enter_action(s):
        # the string is received in all uppercase, converts to lowercase
        # since dictionary is all lowercase
        s = s.lower()
        
        wordleGuessArray = list(s)
        wordleArray = list(rand_word)

        # break random word and guess into component letters
        print(wordleGuessArray)
        print(wordleArray)

        # check if the word is in the list
        if s in FIVE_LETTER_WORDS:
            iCount = 0
            # loop through each letter in both the guess and random word
            while iCount < len(wordleGuessArray):
                # function to color keys green if in correct position
                if wordleGuessArray[iCount] == wordleArray[iCount]:
                    #print("Correct position" + wordleGuessArray[iCount])
                    i = gw.get_current_row()
                    gw.set_square_color(i, iCount, CORRECT_COLOR)
                    wordleArray[iCount] = ""
                # fuction to color keys yellow if guessed letter is in random word
                elif wordleGuessArray[iCount] in wordleArray:
                    i = gw.get_current_row()
                    gw.set_square_color(i, iCount, PRESENT_COLOR)
                # function to color keys grey if guessed letter not in random word
                else:
                    #print("Not correct position" + wordleGuessArray[iCount])
                    i = gw.get_current_row()
                    gw.set_square_color(i, iCount, MISSING_COLOR)
                iCount += 1

        # if correct, display the following
        if s == rand_word:
            gw.show_message("Correct!")
            i = 6
            gw.set_current_row(i)
        # if in the list, display the following
        elif s in FIVE_LETTER_WORDS:
            gw.show_message("You're headed in the right direction!")
            i = gw.get_current_row()
            i = i+1
            if i == N_ROWS:
                gw.show_message("Sorry, it was " + rand_word)
            else:
                gw.set_current_row(i)
        # if not in the list, display the following
        else:
            gw.show_message("Not in word list")

    gw = WordleGWindow(rand_word)
    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()
