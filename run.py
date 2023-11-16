"""
Gets word/hint pairs and images from other .py files
"""
import random
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
        # Spaces out the letters and underscores
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
        self.guesses.append(guess)
        self.check_letter(guess)

    def check_letter(self, data):
        """
        Checks if the letter is in the word.
        Returns the index of the first item that is equal to data.
        """
        if data not in self.word:
            self.tries -= 1
            print(10*"\n")
            print(
                f"Sorry, that letter is not in the word.\n"
                f"You have {self.tries} more chances."
            )

        while data in self.word:
            i = self.word.index(data)
            self.secret_word[i] = data
            self.word[i] = "."
            print(10*"\n")
            print(
                f"Great job! You have {self.tries}"
                f" more chances."
            )

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
# Inspired by Hangman Game by Klara Martinsson

    """
    Welcomes the player by name, shows the rules.
    """
    print("\nWelcome to Snowy Melt!")

    while True:
        name = input("What's your name? \n")
        if not name.isalpha():
            print(f"\nInvalid name, please enter your name.")
        else:
            break

    print(
        f"\nHi {name}! To play, guess the letters in the mystery word.\n"
        "You get 5 incorrect guesses before Snowy melts away...\n")

    input(f"Are you ready? Press Enter to start the game!\n")

    """
    Starts the game.
    """
    while True:
        """
        Gets a random word/hint pair from the dictionary.
        """
        # Code suggested by a resource from tutoring (Rebecca)
        word, hint = random.choice(list(word_hint.items()))
        word = word.upper()

        player = Snowy(name, word, hint)
        while True:
            """
            Runs game until the word is complete or 5x wrong guesses.
            """
            player.start_game()
            player.guess_letter()
            if player.word_complete():
                print(
                    """
                    \n
                        *     *
                    *      *    *
                      *       *
                       _|=|_   *
                    *  ('<')
                    >—(  o  )—<
                     (   o   )  *
                    (    o    )
                    -----------
                    """
                )
                print(f"\nYou win, {name}! The word is: {word.upper()}\n")
                break
            if player.check_tries():
                print(
                    f"\nSorry {name}, you lose.\n"
                    f"The word is: {word.upper()}\n")
                break

        input(f"Hey, it's snowing! Press Enter to play again.\n")


main()
