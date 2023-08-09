from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = 1  # horizontal movement
        self.dy = 1  # vertical movement

    def move_left(self):
        new_x = self.xcor() - self.dx
        new_y = self.ycor() - self.dy
        self.goto(new_x, new_y)
        
    def move_right(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)    

    def bounce_y(self):
        self.dy *= -1  # reverse vertical direction

    def bounce_x(self):
        self.dx *= -1  # reverse horizontal direction
        
    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
