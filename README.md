---- Overview: ----The project is about Sliding Puzzle Game. The game only supports Python, and it has Fifteen, Luigi, Mario, Smiley, Yoshi, and any other type of slide puzzle game. Personally, l learned about making images into the puzzle, so I would recommend it to anyone who wants to start building puzzle games from the basics to becoming a pro.


---- Design: ----In this project, we used a procedural approach to solve the slide puzzle game that can load several puzzle games. From the beginning, we create a function that displays the splash of “CS 5001 ALIGN SLIDE PUZZLE”. We prompt the player through the turtle dialogue box to input their names and number of moves compared to getting an onscreen click to move tiles from adjacent to a blank square. Tiles that are clicked shift to where the blank was, and the empty changes to where the clicked Tile was. While the game state is playing, the status line in the game is updated when each move is completed. Then we set the condition that if the player uses more movements than the max moves they have selected, they lose the game; otherwise, if the player unscrambles the puzzle in fewer moves than specified, they win the game. For both conditions, we set a popup window that tells the players if they win or lose and if there is an error loading their preferred game. For some players that get frustrated while finding it challenging to unscramble, we created functions for Reset Button that display the puzzle in its completed form. There is also function log errors encountered, and we designed a function Quit button which enables players to quit the puzzle


---- Source Files: ----
 
- Tiles images, 
- Puzzle metadata (fifteen.puz, Luigi.puz, mario.puz, malformed_mario.puz, smiley.puz), 
- Resources images that send the user a message.
 


---- Citations/References/Shoutouts ----
 
- Cited: Stackoverflow.com- Also, I Collaborated with the outstanding TAs. They support effortlessly.

