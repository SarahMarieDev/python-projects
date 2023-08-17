import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# TODO 2: Create a turtle player that starts at the bottom of the screen
player = Player()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.exitonclick()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

# TODO 3: Listen for the "Up" keypress to move the turtle north.


# TODO 4: Create and move the cars


# TODO 6: Detect collision with car


# TODO 8: Create scoreboard


# TODO 9: Detect collision with finish line


# TODO 10: Create a "Level" and increase difficulty
