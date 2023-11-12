# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
import os
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

    
    # Don't un-comment this because right now it prints forever
    def start_game(self):
        print("The game is starting")
    #     print(snowy_image(self.tries))
    #     print(*self.secret_word)
    #     print(*self.guesses)

    def validate_guess(self, data):
        """
        Checks the input to validate that it is one letter.
        """
        try:
            if not data.isalpha():
                raise ValueError(
                    f"You entered: {data}. Please enter a letter")
            if len(data) != 1:
                raise ValueError(
                    f"You entered: {data}. Please enter only one letter")
            if data in self.guesses:
                raise ValueError(f"You already guessed: {data}")
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.\n")
            return False
        return True

    def guess_letter(self):
        """
        If validate_guess function comes back as false player get to
        guess the letter again, otherwise the loop breaks.
        """
        while True:
            guess = input("Guess a letter: ").upper()
            if self.validate_guess(guess):
                break
        # Adds the guessed letter to the list of guesses
        self.guesses.append(guess)
        # Checks if the letter is in the word
        self.check_letter(guess)

    def check_letter(self, data):
        """
        Checks if the letter is in the word.
        Returns the index of the first item that is equal to data.
        """
        if data not in self.word:
            self.tries -= 1
            print(
                10*"\n", f"Sorry that letter is not in the word. You have {self.tries}"
                " more chances.")

        while data in self.word:
            i = self.word.index(data)
            self.secret_word[i] = data
            self.word[i] = "."
            print(
                10*"\n", f"Great job! You have {self.tries}"
                " more chances.")

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
    word_input = random.choice(words).upper()
    print(words)

    player = Snowy(name, word_input)
    while True: 
        """
        Keeps the game running until word is completed.
        """
        player.start_game()
        player.guess_letter()
        break
    
main()

