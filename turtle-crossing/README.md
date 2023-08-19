# Turtle Crossing Game

Today I started building the Turtle Crossing game.  I started by breaking down the project and writing my TODOs.  

I first created the player turtle, positioned it at the bottom of the screen and added a listener to listen for the “Up” key to move the turtle forward by pressing the “Up” key.

Next, I built the CarManager class.  Here I created an empty array for the new cars that are created to get added to. I also created methods for moving the cars, increasing the speed when leveling up and removing offscreen cars to save memory.

Finally I created the scoreboard class and added logic to increase the score if the player makes it through, increase the speed of the cars for every level up and detect if there is a collision with a car to trigger the game over sequence.

Although not apart of the project instructions, I decided to add the capability to move the turtle backwards as well as forwards to make the game a little more fun.

## Key Concepts

1. **Object-Oriented Programming (OOP)**:
    - **Classes and Objects**: The program demonstrates how to use classes to encapsulate data and behavior. Creating an object of these classes allows for representing and controlling game elements, such as cars and the player's character.
    - **Encapsulation**: The classes provide an example of encapsulation. They hide the implementation details and expose only the necessary methods. This approach keeps the main game loop clean and straightforward.
2. **Game Loop**:
    - A fundamental concept in most video games and simulations. The game loop repeatedly checks for user inputs, updates the game state, and renders the game display. In the context of the turtle road crossing game, each iteration of the loop might involve creating new cars, moving existing cars, checking for collisions, updating the game's level, etc.
3. **Collision Detection**:
    - Collision detection ensures that the game responds appropriately to in-game events, such as the player's character getting hit by a car, which triggers the game over sequence

## Challenges Experienced

First challenge was figuring out how to create multiple cars with different positions and colors.

I solved this by creating a CAR_CREATION_RATE variable and put it as a condition in an if statement for creating the cars so that a car is not created on every loop of the game.

Next challenge I had was after finishing the program, the scoreboard was not clearing when I leveled up and it did not seem to level up past 2.  After coming back to the project I noticed that my scoreboard initializer was in the while loop. I moved it to outside of the while loop and now everything works as expected.