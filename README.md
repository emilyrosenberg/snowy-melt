<!-- ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding! -->

# ❄️ Snowy Melt

<!-- Mockup -->

Snowy Melt is a mystery-word guessing game for one player. It is written as a Python command-line game. Based on a hint and the word length, the player guesses letters to complete the word. With each wrong guess, Snowy the snowman melts away.<br>
The game is designed to be fun and entertaining for people of every age and ability.

## Features 

<!-- In this section, you should go over the different parts of your project, and describe each in a sentence or so. You will need to explain what value each of the features provides for the user, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things. -->

### Current features

Greeting <br>
At the beginning of the game, the user inputs their name. Then they see a persoanlized greeting and an explanation of the rules.<br>

Start <br>
A random word/hint pair is pulled from the dictionary. The user sees the snowman character, underscores representing letters in the mystery word, a hint to help them guess, and a prompt to guess a letter. <br>

Play <br>
When the user guesses a letter, the input is validated and the game provides feedback. If the letter is in the word, it is added to the board. If not, the snowman melts down one level. <br>

End <br>
After the mystery word is solved or the player runs out of guesses, the game shows win or lose feedback with special graphics for each, and gives the user an option to play again.

### Design
I used Lucidchart to design the flow of this game's functions. <br> ![Flow chart](readme-images/flow-chart.png)

<!-- - __Navigation Bar__

  - Featured on all three pages, the full responsive navigation bar includes links to the Logo, Home page, Gallery and Sign Up page and is identical in each page to allow for easy navigation.
  - This section will allow the user to easily navigate from page to page across all devices without having to revert back to the previous page via the ‘back’ button. 

![Nav Bar](https://github.com/lucyrush/readme-template/blob/master/media/love_running_nav.png)

- __The landing page image__

  - The landing includes a photograph with text overlay to allow the user to see exactly which location this site would be applicable to. 
  - This section introduces the user to Love Running with an eye catching animation to grab their attention

![Landing Page](https://github.com/lucyrush/readme-template/blob/master/media/love_running_landing.png)

- __Club Ethos Section__

  - The club ethos section will allow the user to see the benefits of joining the Love Running meetups, as well as the benefits of running overall. 
  - This user will see the value of signing up for the Love Running meetups. This should encourage the user to consider running as their form of exercise. 

![Club Ethos](https://github.com/lucyrush/readme-template/blob/master/media/love_running_ethos.png)

- __Meetup Times section__

  - This section will allow the user to see exactly when the meetups will happen, where they will be located and how long the run will be in kilometers. 
  - This section will be updated as these times change to keep the user up to date. 

![Meetup Times](https://github.com/lucyrush/readme-template/blob/master/media/love_running_times.png)

- __The Footer__ 

  - The footer section includes links to the relevant social media sites for Love Running. The links will open to a new tab to allow easy navigation for the user. 
  - The footer is valuable to the user as it encourages them to keep connected via social media

![Footer](https://github.com/lucyrush/readme-template/blob/master/media/love_running_footer.png)

- __Gallery__

  - The gallery will provide the user with supporting images to see what the meet ups look like. 
  - This section is valuable to the user as they will be able to easily identify the types of events the organisation puts together. 

![Gallery](https://github.com/lucyrush/readme-template/blob/master/media/love_running_gallery.png)

- __The Sign Up Page__

  - This page will allow the user to get signed up to Love Running to start their running journey with the community. The user will be able specify if they would like to take part in road, trail or both types of running. The user will be asked to submit their full name and email address. 

![Sign Up](https://github.com/lucyrush/readme-template/blob/master/media/love_running_signup.png)

For some/all of your features, you may choose to reference the specific project files that implement them.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future: -->

### Future implementations

- Feedback about how many guesses the user took to win
- A more advanced scoring system

## Technologies used
Python <br>
Lucidchart <br>
Heroku <br>
Github <br>
Git <br>
Gitpod

## Testing 
This game was tested throughout development in the terminal in VS Code, and in a deployed version using Heroku.

### Bugs
Here are a few of the bugs I dealt with during development.
- Press any key to start the game <br>
I researched a tried several ways to implement this, including import keyboard and using various functions which did not work for me. But then I found other advice arguing that using the input() function was probably the best solution in Python. The result was that the user presses Enter to start the game and play again.
- Get word/hint pairs from a dictionary <br>
Originally I had a list of words and a list of hints, but I needed them to be connected so that the pair showed in the same round of the game. My mentor helped me create a dictionary of pairs instead of two lists. Code Institute tutoring (Rebeccca) directed me toward a [resource](https://stackoverflow.com/questions/4859292/how-can-i-get-a-random-key-value-pair-from-a-dictionary/4859322#4859322) so that I could get a random pair first. Then I figured out how to get the word and the hint from there, and send them to the right place.
- The upper() function <br>
In order for the guessed letter to be validated, both the guess and the letters in the word must be uppercase. At first I didn't understand where this function should go. I did a lot of trial and error, and printing. After I changed the functionality of getting the word/hint pairs, I had to figure it out again.
- Re-starting the game <br>
I researched more about how to re-start the game using a while loop, and found [this resource](https://www.askpython.com/python/examples/restart-loop-in-python#:~:text=Restart%20a%20Nested%20Loop%20in%20Python&text=A%20nested%20loop%20is%20a,will%20understand%20this%20during%20implementation.) helpful.

<!-- In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your project’s features and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here. -->

### Code Validation 

I validated the app with the [Code Institute Python Linter](https://pep8ci.herokuapp.com/). The errors were blank spaces, incorrect indentation, and lines that were too long. There are now no errors.<br> ![Linter result](readme-images/linter-result.png)

### Unfixed Bugs

<!-- You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.  -->

## Deployment

This app was deployed using Heroku. The live link can be found [here](https://snowy-melt-ad37e9d6291f.herokuapp.com/).

## Finished game
<!-- Screenshots -->

## Credits 
- This game was inspired by the [Hangman Game by Klara Martinsson](https://github.com/KlaraMartinsson/hangman-game/tree/main) which was provided as an example by my cohort facilitator, David Calikes. I used this example to create the structure of my project, and added my own ideas and functionality.
- The idea for a word-guessing game featuring a snowman came from [this website](https://rhodygirlresources.com/product/digital-sight-word-games-snowman-melt/).
- The ascii character was inspired by images [here](https://amgrubb.github.io/csc111/lab-5-loopFunc.html) and [here](https://www.momsarefrommars.com/moms-blog/category/ascii%20art).
- The words and definitions were adapted from content found in [Weather Words](https://www.metoffice.gov.uk/weather/learn-about/met-office-for-schools/other-content/other-resources/weather-words) and [EnglishClub Weather Vocabulary](https://www.englishclub.com/vocabulary/weather-vocabulary.php).

Thank you to my mentor,

This [resource](https://stackoverflow.com/questions/4859292/how-can-i-get-a-random-key-value-pair-from-a-dictionary/4859322#4859322) for accessing a random pair was provided by CI tutoring (Rebecca).



<!-- In this section you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 

You can break the credits section up into Content and Media, depending on what you have included in your project.  -->

### Content 

<!-- - The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/) -->

### Media

<!-- - The photos used on the home and sign up page are from This Open Source site
- The images used for the gallery page were taken from this other open source site


Congratulations on completing your Readme, you have made another big stride in the direction of being a developer!  -->

<!-- ## Other General Project Advice -->

<!-- Below you will find a couple of extra tips that may be helpful when completing your project. Remember that each of these projects will become part of your final portfolio so it’s important to allow enough time to showcase your best work! 

- One of the most basic elements of keeping a healthy commit history is with the commit message. When getting started with your project, read through [this article](https://chris.beams.io/posts/git-commit/) by Chris Beams on How to Write  a Git Commit Message 
  - Make sure to keep the messages in the imperative mood 

- When naming the files in your project directory, make sure to consider meaningful naming of files, point to specific names and sections of content.
  - For example, instead of naming an image used ‘image1.png’ consider naming it ‘landing_page_img.png’. This will ensure that there are clear file paths kept. 

- Do some extra research on good and bad coding practices, there are a handful of useful articles to read, consider reviewing the following list when getting started:
  - [Writing Your Best Code](https://learn.shayhowe.com/html-css/writing-your-best-code/)
  - [HTML & CSS Coding Best Practices](https://medium.com/@inceptiondj.info/html-css-coding-best-practice-fadb9870a00f)
  - [Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html#General)

Getting started with your Portfolio Projects can be daunting, planning your project can make it a lot easier to tackle, take small steps to reach the final outcome and enjoy the process!  -->