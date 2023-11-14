# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

"""
Get words, hints, and images from other .py files
"""

# import random
# import keyboard
from words_list import word_hint
from snowy_image import snowy_image

class Snowy:
    # Inspired by Hangman Game by Klara Martinsson
    """
    Holds details to create and play the game.
    """

    def __init__(self, name, word, hint):
        self.name = name
        self.word = [x for x in word]
        self.hint = hint
        # Holds already-guessed letters
        self.guesses = []
        self.tries = 5
        # Shows _ for each letter.
        self.secret_word = len(self.word)*["_"]

    def start_game(self):
        print(snowy_image(self.tries))
        print(*self.secret_word)
        print(*self.guesses)
        print(f"\nHint: ")
        print(self.hint)
      
    def validate_guess(self, data):
        """
        Checks the input to make sure it is one letter.
        """
        try:
            if not data.isalpha():
                raise ValueError(
                    f"You entered: {data}. Please enter a letter")
            if len(data) != 1:
                raise ValueError(
                    f"You entered: {data}. Please enter only one letter")
            if data in self.guesses:
                raise ValueError(f"You already entered: {data}")
        except ValueError as e:
            print(f"Invalid input: {e}.\n")
            return False
        return True

    def guess_letter(self):
        """
        Takes the input, makes it uppercase and adds it to the list of guesses.
        Sends it to be validated.
        """
        while True:
            guess = input("\nGuess a letter: \n").upper()
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
                10*"\n", f"Sorry, that letter is not in the word. You have {self.tries}"
                " more chances.")

        while data in self.word:
            i = self.word.index(data)
            self.secret_word[i] = data
            self.word[i] = "."
            print(
                10*"\n", f"Great job! You have {self.tries}"
                " more chances.")
            
    def word_complete(self):
        """
        Checks for remaining "_".
        If none remain, the word is completed.
        Otherwise the game continues.
        """
        if "_" not in self.secret_word:
            self.start_game()
            return True

    def check_tries(self):
        if self.tries <= 0:
            self.start_game()
            return True

def main():

    """
    Welcomes the player by name, shows the rules.
    """
    print("\nWelcome to Snowy Melt!")

    # Name validation from Hangman Game by Klara Martinsson
    while True:
        name = input("What's your name? \n")
        if not name.isalpha():
            print(f'\nInvalid name, please enter your name.')
        else:
            break
    
    print(f"\nHi {name}! To play, guess the letters in the mystery word.\nYou get 5 incorrect guesses before Snowy melts away...\n")
    
    # Add code to press any key/or to do nothing unless enter is clicked
    # start_game = input("fAre you ready? Press Enter to start the game!\n")
    # print("fAre you ready? Press any key to start the game!\n")
    # keyboard.wait()
    # print("You pressed a key")
    print(f"Are you ready? Press Enter to start the game!\n")
    input()
    

    # Code to get words and hints suggested by my mentor
    """
    Gets a word and displays it in uppercase.
    """
    keys = list(word_hint.keys())
    word = keys[9].upper()
    """
    Gets a hint.
    """
    for i in word_hint:
        hint = word_hint[i]

    player = Snowy(name, word, hint)
    while True: 
        """
        Runs the game until the word is completed or there are no more tries.
        """
        player.start_game()
        player.guess_letter()
        if player.word_complete():
            # Add code to print first (unmelted) Snowy image
            print(f"\nYou win, {name}! The word is: {word.upper()}\n")
            break
        if player.check_tries():
            print(f"\nSorry {name}, you lose. The word is: {word.upper()}\n")
            break
    
    input(f"Hey, it's snowing! Press Enter to play again.\n")
    # Add code to press any key/or to do nothing unless enter is clicked
    # Add code to play again
    

main()