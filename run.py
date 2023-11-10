# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def start():
    """
    Welcomes the player by name, shows the rules
    """
    print("\nWelcome to Snowy Melt!")
    name = input("What's your name? ")
    print(f"\nHi {name}! To play, guess the letters in the mystery word.\nYou get 5 incorrect guesses before Snowy melts away…\n")
    start_game = input("Are you ready? (Y/N)\n")
    
start()
