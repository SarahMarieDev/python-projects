# Pong Game

### 08-07-2023:

Today I started working on the Pong game project. First, I created the screen for the game with the usual setup and set the size and color.

Next, I created the Paddle class which inherits from the Turtle class. I wrote the code to create a paddle take in a position argument so that I can reuse the code to create multiple paddles in different positions.

Then I created the functions and event listeners to allow the paddles to move by using the up/down keys for the right paddle and “w”/”s” keys for the left paddle.

### 08-08-2023:
Created the ball class, initialized the ball and created a move() method to make the ball move up and to the right.  I initially used the time.sleep() method to slow it down and moved it by 10 px each time, but it looked a little choppy and I couldn’t get it to hit the border exactly so I removed the time.sleep() method and changed the movement to 1px at a time which resulted in a smoother looking movement and more precise contact with the wall.

I then created the bounce() method so that the ball would bounce off the top or bottom of the screen. I had some challenges with that described below.

### 08-09-2023:
Today I finished the pong game. I wrote the code to detect a collision with either of the paddles, detect when the paddle misses and keep the score.

I didn’t really experience too many challenges today. The only thing I couldn’t figure out was to keep my ball moving by 1px only and still increase the speed with every turn. So I ended up modifying it back the original way at 10px and using the time.sleep() method.

I created the game over sequence to be when one player gets a score of 10, then the program ends.

## Challenges experienced

### 08-08-2023
My first major challenge was getting the ball to “bounce” off the wall.  Here is my current code:

```python
# in the Ball class
def bounce(self):
		new_y = self.ycor() - 1
    self.goto(self.xcor(), new_y)

# in main.py
if ball.ycor() > 285 or ball.ycor() < -285:
     screen.update()
     ball.bounce()
```

Currently, the behavior of the ball is when it hits the top of the screen it just continues to the right  sort of sliding against the border of the screen.

I resolved this challenge by creating variables in the initializer to represent the change in x and y values. Then I updated the move() method to add those variables instead of my hardcoded number.

For the bounce() method, I changed it to multiply the current y coordinate by -1 which will reverse the movement.

1. If **`self.dy`** is positive (meaning the ball is moving upward), multiplying it by **`1`** makes it negative, so the ball will start moving downward.
2. If **`self.dy`** is negative (meaning the ball is moving downward), multiplying it by **`1`** makes it positive, so the ball will start moving upward.

```python
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = 1 # horizontal movement
        self.dy = 1 # vertical movement

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

    def bounce(self):
        self.dy *= -1 # reverse vertical direction
```
