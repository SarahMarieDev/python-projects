from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move_right()

    # Detect collision with wall and bounce
    if ball.ycor() > 285 or ball.ycor() < -285:
        screen.update()
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 330 or ball.distance(left_paddle) < 30 and ball.xcor() < -330:
        ball.bounce_x()

    # Detect if ball goes out of bounds on right side
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    # Detect if ball goes out of bounds on left side
    if ball.xcor() < -380:
        ball.reset_position()
        ball.move_speed = 0.1
        scoreboard.right_point()

    if scoreboard.left_score == 10 or scoreboard.right_score == 10:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
