# Ping
The game of ping, similar to but legally distinct from pong.

## Installation
1.	If you don't have any version of Python 3 installed on your computer, download the latest version of Python (https://www.python.org/downloads/release/python-380/);
2.	If you don't have Pygame installed on your computer, download the latest version of Pygame by following steps from http://kidscancode.org/blog/2015/09/pygame_install/;
3.	Clone our repository 5oclock_ping_game or download ZIP from the following link: https://github.com/hohloval/5oclock_ping_game;
4.	Run main.py to launch "Ping".

## How To Play
1.	Main Menu screen:
-	Select score limit option:
	-	10 is the default score limit;
	-	Increase/decrease the limit by 1 by pressing "up"/"down" buttons;
	-	Choose Infinite mode option by pressing "Infinite mode" button;
-	Start the game by pressing "Two player game".

2.	Game field screen:
-	Press "SPACE" key to start playing;
-	Player 1 moves the left paddle up/down by pressing "w"/"s" keys, Player 2 – "Up"/"Down";
-	Press "MENU" button to return to the main menu screen​;
-	Press "p" key to pause the game and "r" to resume the game;
-	Press "h" key to play again​ after the game is over.

3.	Rules:
-	A player gets a score point when the ball hits opponent's boarder;​
-	Move your paddle to reflect the ball​ and defend your border;
-	Player wins when reaches the score limit​.

## Documentation and Directory Structure
head over to the wiki page of this project for information on our project structure and documentation.
[here](https://github.com/hohloval/5oclock_ping_game/wiki)

## Authors
Ping is a game designed by 2nd year cs students at University of Toronto Mississauga. This project was done for the course CSC290: Communication Skills for Computer Scientists. Here are the group members:
-	Alexandr Hohlov
-	Salman Azhar
-	Ekaterina Semyanovskaya
-	Erin Amer

## Licensing
The MIT License

Copyright (c) [2019] [Alexandr Hohlov, Salman Azhar, Ekaterina Semyanovskaya, Erin Amer]

You can find a copy of the license in the LICENSING.txt file [here](https://github.com/hohloval/5oclock_ping_game/blob/master/LICENSING.txt)

This license is in Public Domain.

## Individual Contributions

### Alexandr Hohlov
Wrote and implemented the Message, ScoreBoard and HighScore classes into the game and main menu. Added a random ball angle when the ball bounces off the player paddles. I also smoothed out the movement of the ball and paddle. 

For the README, I setup the format, and acquired the MIT license. For the wiki, I setup the wiki format, wrote the main page and file structure page. For the class description page I wrote the Game, Actor, Subclasses of Actor, HighScore and UML Diagram sections. 

### Salman
For the application, I added the boundaries and implemented the ball movement and its behaviour for interacting with the various actors. I also implemented the play/pause feature.

For the READEME, I provided two examples of how a user can extend the game. These examples were cosmetic or functional (affects gameplay). To show these extended features in action, i also added gif files demonstrating their implemeneted forms.

### Ekaterina
insert text here

### Erin
For the code, I implemented the MainMenu and Button classes. The MainMenu class displays multiple buttons that let the players choose what they want the score limit to be. It also displays a button that lets them start the game. The buttons can be customized to run any function on any Pygame surface, so they can be reused in any project. For the Project Repository, I added the descriptions in the wiki for the MainMenu and Button classes. I also proofread and edited multiple pages on the wiki and README.
