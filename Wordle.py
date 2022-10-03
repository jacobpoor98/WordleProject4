# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, WordleSquare

def wordle():
    # selects a random word from the wordle dictionary
    rand_word = random.choice(FIVE_LETTER_WORDS)
    print(rand_word)


    

    def enter_action(s):
        # the string is received in all uppercase, converts to lowercase
        # since dictionary is all lowercase
        s = s.lower()
        # check if the word is in the list
        if s == rand_word:
            gw.show_message("Correct!")
        elif s in FIVE_LETTER_WORDS:
            # if in the list, display the following
            gw.show_message("You're headed in the right direction!")
        else:
            # if not in the list, display the following
            gw.show_message("Not in word list")

    gw = WordleGWindow(rand_word)
    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()
