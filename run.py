# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# import random
# import os
from words_list import words, hints
from snowy_image import snowy_image

class Snowy:
    # From Hangman Game by Klara Martinsson
    """
    Holds details to create and play the game.
    """
# Need to add code to show the hint, show the already-guessed letters, and loop through the game after a letter is guessed
# Need to add win/lose code, and to display the "it's snowing" end screen

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
                raise ValueError(f"You already guessed: {data}")
        except ValueError as e:
            print(f"Invalid input: {e}.\n")
            return False
        return True

    def guess_letter(self):
        """
        If validate_guess function comes back as false player get to
        guess the letter again, otherwise the loop breaks.
        """
        while True:
            guess = input("\nGuess a letter: ").lower()
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
                f"\nSorry that letter is not in the word. You have {self.tries}"
                " more chances.")

        while data in self.word:
            i = self.word.index(data)
            self.secret_word[i] = data
            self.word[i] = "."
            print(
                f"\nGreat job! You have {self.tries}"
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
    Gets a word from the list of words and displays it in uppercase
    """
    # Not working yet, doesn't get "word" or convert to uppercase
    for word in words:
        print(word)
  
    for hint in hints:
        print(hint)

    player = Snowy(name, word, hint)
    while True: 
        """
        Keeps the game running until word is completed.
        """
        player.start_game()
        player.guess_letter()
        if player.word_complete():
            # Add code to print first (unmelted) Snowy image
            print(f"You win, {name}! The word is: {word}\n")
            break
        if player.check_tries():
            print(f"Sorry {name}, you lose. The word is: {word}\n")
            break
    
    input(f"It's snowing... press Enter to play again")
    # Add code to play again

main()

