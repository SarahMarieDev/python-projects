from turtle import Turtle, Screen
import random

tim = Turtle()


# tim.color("dark turquoise")
# tim.pencolor("blue violet")

# # draw square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
#
# tim.up()
# tim.setposition(-50, 50)
#
# # draw a dashed line
# for _ in range(20):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#
# tim.clear()
# tim.up()
# tim.setposition(-50, 50)

def change_color():
    r = random.random()
    b = random.random()
    g = random.random()
    random_color = (r, b, g)
    return random_color


# # drawing different shapes
# def draw_shape(num_of_sides):
#     angle = 360 / num_of_sides
#     for _ in range(num_of_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     change_color()
#     draw_shape(shape_side_n)

# # Draw a random walk
# def go_left():
#     tim.left(90)
#     tim.forward(25)
#
#
# def go_right():
#     tim.right(90)
#     tim.forward(25)
#
#
# def turn_around():
#     tim.right(180)
#     tim.forward(25)


# Alternate solution (probably better since less code)
# directions = [0, 90, 180, 270]
# for _ in range(100):
#   tim.forward(25)
#   tim.setheading(random.choice(directions))

# tim.pensize(15)
# tim.speed("fastest")
# for _ in range(200):
#     tim.color(change_color())
#     direction = random.randrange(0, 4)
#     match direction:
#         case 0:
#             tim.forward(25)
#         case 1:
#             turn_around()
#         case 2:
#             go_left()
#         case 3:
#             go_right()

# # Draw a Spirograph
tim.speed("fastest")


def draw_spirograph(gap_size):
    for heading in range(0, 360, gap_size):
        tim.setheading(heading)
        tim.color(change_color())
        tim.circle(100)
        tim.circle(80)
        tim.circle(50)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
