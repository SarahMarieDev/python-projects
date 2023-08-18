import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create the player turtle
player = Player()

 # TODO 3: Create the cars
car_group = CarManager()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    
   
    

    # Move the player turtle
    screen.listen()
    screen.onkey(player.move, "Up")


# TODO 4: move the cars


# TODO 6: Detect collision with car


# TODO 8: Create scoreboard


# TODO 9: Detect collision with finish line


# TODO 10: Create a "Level" and increase difficulty

screen.exitonclick()