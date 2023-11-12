# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random


def start():
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

def start_game():
    print("The game is starting")


    
start()
start_game()
