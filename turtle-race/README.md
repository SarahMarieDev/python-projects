# Turtle Race Game
The final project of the day was the turtle race. I took it a step further at the end and decided to show the user an alert box telling them if they won or lost, instead of printing it to the console. I did this using the Python interface _tkinter_ and displaying the message with the color that won by putting the message into a variable.
We learned a lot about the turtle coordinate system which I was actually able to figure out on my own in prior lessons due to my experience with graphs in math.
  

## Key concepts
- Functions as inputs. We can pass a function into another function’s input parameter. Only pass name, not parentheses. The function that can take another function as input is known as a Higher Order Function.
- When using an event listener, we use keyword arguments vs positional arguments.
- Objects and instances (separate copies of the same class that can have different attributes & methods) This is also known as the state.
- Turtle Coordinate System

  

## Challenges experienced
I only had a few challenges during the turtle race project. The main one was figuring out how I was going to create multiple instances of turtles. I started out thinking about the normal way of doing this with classes with the init and then naming them all different variable names. I could not figure out a way to do that so I finally went to the video for a hint. Once I found that she created lists for the turtle instances and the y values, I was able to pick up in that direction and write the code out by myself.

The only other little challenge I had was getting the turtles to stop but then I figured out that the if statement needed to be at the beginning of the for loop instead of at the end, and checking to see if the x-coordinate was greater than 230.
