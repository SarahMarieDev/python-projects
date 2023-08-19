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
car_manager = CarManager()

# TODO: Create scoreboard

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    # Create and move the cars
    car_manager.create_car()
    car_manager.move_cars()
    car_manager.remove_offscreen_cars()

    # Move the player turtle
    screen.listen()
    screen.onkey(player.move, "Up")

    # TODO Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 30:
            game_is_on = False


    # TODO Detect collision with finish line


    # TODO Create a "Level" and increase difficulty

screen.exitonclick()