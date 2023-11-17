# ❄️ Snowy Melt

![Mockup on different devices, created with Techsini.](readme-images/mockup.png)

Snowy Melt is a mystery-word guessing game for one player. It is written as a Python command-line game. Based on a hint and the word length, the player guesses letters to complete the word. With each wrong guess, Snowy the snowman melts away.<br>
You can find the game [here](https://snowy-melt-ad37e9d6291f.herokuapp.com/).

## Features 

The game is designed to be fun for people of every age and ability. Whether the user is learning vocabulary, learning to spell, or just looking for entertainment, this game's input and feedback structure is engaging, and the content is interesting and diverse within its theme.

### Current features

Greeting <br>
At the beginning of the game, the user is introduced to the game's purpose and their goal. After they input their name, they see a personalized greeting, an explanation of the rules, and a prompt to press Enter to start the game.<br>

Start <br>
A random word/hint pair is pulled from the dictionary. The user sees the snowman character, the underscores representing letters in the mystery word, a hint to help them guess, and a prompt to guess a letter. <br>

Play <br>
When the user guesses a letter, the input is validated and the game provides feedback. If the letter is in the word, it is added to the board. If not, the snowman melts down one level. <br>

End <br>
After the mystery word is solved or the player runs out of guesses, the game shows win or lose feedback with special graphics for each, and gives the user an option to play again.

### Design
I designed this game with a weather theme. In a small, simple game like this, a theme makes it more cohesive and fun for the user. It is meant to be entertaining for anyone, so the words are all different lengths, and some of the words and hints are easier than others. The user might not win every round, but the game is designed so that they will always discover something quirky and enjoyable! <br>
I used Lucidchart to design the flow of this game's functions. <br> ![Flow chart](readme-images/flow-chart.png)<br>
I designed this character, "Snowy," based on two different ascii images that I found online (credited below).<br>
![Snowy](readme-images/snowy.png)

### Future implementations
In the future I would like to add more features to this game. For instance:
- Styling
- Feedback about how many guesses the user took to win
- A more advanced scoring system
- Levels of difficulty
- Different themes for the words and images

## Technologies used
Python <br>
Lucidchart <br>
Heroku <br>
Github <br>
Git <br>
Gitpod

## Testing 
This game was tested throughout development in the terminal in VS Code. It was deployed and tested using Heroku.

### Functionality
The game is written in a run.py file, and the images and word/hint pairs are stored in two other .py files. These files are imported into the main file, which gets a random word/hint pair for each round, and iterates through the images to show the user the visual of a melting snowman. This functionality is designed to be simple and to run without errors.

### Bugs
Here are a few of the bugs I fixed during development.
- Press any key to start the game <br>
I researched and tried several ways to implement this, including "import keyboard" and using various functions which did not work for me. But then I found other advice arguing that using the "input()" function was probably the best solution in Python. The result is that in the finished game the user presses Enter to start the game and to play again.
- Get word/hint pairs from a dictionary <br>
Originally I had a list of words and a separate list of hints, but I needed them to be connected so that the pair showed in the same round of the game. My mentor helped me create a dictionary of pairs instead of two lists. Code Institute tutoring (Rebeccca) directed me toward a [resource](https://stackoverflow.com/questions/4859292/how-can-i-get-a-random-key-value-pair-from-a-dictionary/4859322#4859322) so that I could get a random pair first. Then I figured out how to get the word and the hint from there, and send them to the right place.
- The upper() function <br>
In order for the guessed letter to be validated, both the guess and the letters in the word must be uppercase. At first I didn't understand where this function should go. I did a lot of trial and error, and printing. After I changed the functionality of getting the word/hint pairs, I had to figure it out again.
- Re-starting the game <br>
I researched more about how to re-start the game using a while loop, and found [this resource](https://www.askpython.com/python/examples/restart-loop-in-python#:~:text=Restart%20a%20Nested%20Loop%20in%20Python&text=A%20nested%20loop%20is%20a,will%20understand%20this%20during%20implementation.) helpful.
- Extra space at the beginning of printed text <br>
After running the code through the linter and fixing errors, I tested it again and noticed a space at the beginning of some lines of feedback. I fixed this by creating two separate print statements: one for the lines that create space in the terminal for the next guess, and one for the feedback about the correct/incorrect letter and remaining tries.

### Code Validation 

I validated the code in the three .py files with the [Code Institute Python Linter](https://pep8ci.herokuapp.com/). The errors were blank spaces, incorrect indentation, and lines that were too long. There are now no errors.<br> Code in run.py: ![Linter result1](readme-images/linter-result1.png)<br>Code in snowy_images: ![Linter result2](readme-images/linter-result2.png)<br>Code in words_list: ![Linter result3](readme-images/linter-result3.png)<br>

## Deployment

This game was deployed using Github and Heroku. The deployment terminal is 80 columns by 24 rows, and the game was designed to fit this format. The live link can be found [here](https://snowy-melt-ad37e9d6291f.herokuapp.com/).

## Finished game
Here are some screenshots of the finished deployed game. <br>
![Start](readme-images/screenshot0.png) ![Enter username](readme-images/screenshot1.png) ![First guess](readme-images/screenshot2.png) ![Next guess](readme-images/screenshot3.png) ![Win](readme-images/screenshot4.png) ![Wrong guess](readme-images/screenshot5.png) ![Next wrong guess](readme-images/screenshot6.png) ![Lose](readme-images/screenshot7.png)

## Credits 
- This game was inspired by the [Hangman Game by Klara Martinsson](https://github.com/KlaraMartinsson/hangman-game/tree/main) which was provided as an example by my cohort facilitator, David Calikes. I used this example to create the structure of my project, and I'm grateful to the coder for helping me learn!
- I was also inspired by the hangman game example [here](https://hackr.io/blog/python-projects).
- The idea for a word-guessing game featuring a snowman came from [this website](https://rhodygirlresources.com/product/digital-sight-word-games-snowman-melt/).
- The ascii character was inspired by images [here](https://amgrubb.github.io/csc111/lab-5-loopFunc.html) and [here](https://www.momsarefrommars.com/moms-blog/category/ascii%20art).
- The words and definitions were adapted from content found in [Weather Words](https://www.metoffice.gov.uk/weather/learn-about/met-office-for-schools/other-content/other-resources/weather-words) and [EnglishClub Weather Vocabulary](https://www.englishclub.com/vocabulary/weather-vocabulary.php).
- This [resource](https://stackoverflow.com/questions/4859292/how-can-i-get-a-random-key-value-pair-from-a-dictionary/4859322#4859322) for accessing a random pair was provided by CI tutoring (Rebecca).
- I would like to thank my Code Institute mentor, Adegbenga Adeye, for ideas, patience, and support.
- Thanks to my cohort facilitator, David Calikes, for kind and helpful reassurance, and great ideas for future implementations.
- Thanks also to my fellow students, who have been helpful and supportive during this project.