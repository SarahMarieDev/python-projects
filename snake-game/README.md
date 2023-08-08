# Snake Game

## Part 1:

Today I started the Snake game project. I first created the snake body using
a loop to create 3 “Turtle” objects. Then I got them to move together using
the tracer method to turn off the animation and update method to update the
position of all three objects at the same time so that it appears like a
smooth snake movement. The last part I worked on today was creating controls
for the snake so that we can use the arrow keys to make the snake move in
the direction we want. I refined it a bit to make sure that the snake can’t
go back on itself (i.e., go up if it’s going down, go left if it’s going
right, etc.)

## Part 2:

Today I worked on creating the snake food, detecting collision with the snake food, creating a scoreboard and detecting
collision with the wall to end the game. To create the snake food, I created a new class that inherits from the Turtle
class, configured it’s shape, etc. and created a method that lets it move to random spots on the board. Then I added the
conditional statement in main.py to check if the snake collides with the food object, and then update the score and the
position of the food. Next, I created the scoreboard by creating another class that also inherits from the Turtle class.
Used the write() method and the documentation to add the scoreboard to the top of the screen and update the score each
time the snake gets the piece of food. Finally, I wrote the conditional statement which checks to see if the snake hits
a side of the screen and to then stop the game and write out ‘GAME OVER’.

##### Update 08-02-2023

Finished up the Snake Game. The last portion was to detect collision with the tail. I did this by creating new functions
in snake.py to add a segment and for extending the snake. Then in main.py I called the extend() function whenever the
snake hits a piece of food. Then wrote a loop and if statement to trigger the game over sequence if the head is detected
hitting the tail, excluding the head segment.

After that, I refactored a bit to use the slice() method when detecting collision with the body.

## Key concepts

- tracer() and update methods: I turn the screen.tracer() off `screen.tracer(0)` so that there’s no animation. Then use
  the update() method (outside the for loop, so it updates the position of all the segments at once) and set a timer
  to make it go at a reasonable pace.
- Refactor code to OOP.
- Class Inheritance: classes can inherit attributes and methods from other classes. for ex. you have a Chef class and
  want to create a more specialized chef (such as a pastry chef). The PastryChef class can inherit everything from the
  Chef class so that you don’t have to create it from scratch, and then add the additional attributes/methods.
- List slicing allows us to specify a start and end point in a list or tuple like so `[start:stop:step]`
    - **start**(**optional**)- Starting index value where the slicing of the object starts. Default to 0 if not
      provided.
    - **stop**– Index value until which the slicing takes place.
    - **step (optional)**– Index value steps between each index for slicing. Defaults to 1 if not provided.
- Side Note: I also learned that in Python you can set the starting loop index or the step index to -1 to run through the list
  backwards. I went back and redid my code using the slice method on the Day 7 HackerRank challenge and it worked. 😊🎉

## Challenges experienced

First major challenge was getting the controls that move the snake to work.
I started by creating a dictionary of direction key value pairs.
I was trying to use the `.setheading()` method on self which wasn’t working.
Then I resolved that by changing `self.setheading()` to
`self.segments[0].setheading()` which worked. I decided to get rid of the
dictionary of directions and just code the values in the functions.
This resolved the issue and now the code works as expected.

****Refactor**: I actually changed the `segments[0]` and put it in
the snake attributes as head. I also created the values as constants.

###### Update 07-31-2023:

Challenge I experienced today was getting the score to update after the snake collides with a piece of food. It was
mostly
just the placing of things. I originally initialized a new turtle within the init function in the scoreboard class and
defined the score attribute outside the init function. I removed the creation of the scoreboard from the init
function, and added the score attribute within the init function, created the function update_score and called it after
clearing the scoreboard in main.py.
