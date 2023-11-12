# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
from words_list import words, hints
from snowy_image import snowy_image

class Snowy:
    # From Hangman Game by Klara Martinsson
    """
    Holds details to create and play the game.
    """
    def __init__(self, name, word):
        self.name = name
        self.word = [x for x in word]
        # Holds already-guessed letters
        self.guesses = []  
        self.tries = 5
        # Shows _ for each letter.
        self.secret_word = len(self.word)*["_"]

    def start_game(self):
        print(snowy_image(self.tries))
        print(*self.secret_word)
        print(*self.guesses)

def main():

    """
    Welcomes the player by name, shows the rules
    """
    print("\nWelcome to Snowy Melt!")

    # Name validation from Hangman Game by Klara Martinsson
    while True:
        name = input("What's your name? ")
        if not name.isalpha():
            print(f'\nInvalid name, please enter your name.')
        else:
            break
    
    print(f"\nHi {name}! To play, guess the letters in the mystery word.\nYou get 5 incorrect guesses before Snowy melts away...\n")
        
    start_game = input("Are you ready? Press Enter to start the game!\n")
    # Does this need validation?

    """
    Gets a random word from the list of words and displys it in uppercase
    """
    global word_input

    #Not working yet, doesn't get "word" or convert to uppercase
    word = words in words
    # word_input = random.choice(words).upper()
    print(words)
    
main()

