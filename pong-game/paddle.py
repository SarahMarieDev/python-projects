from turtle import Turtle


class Paddle(Turtle):
    MOVE_DISTANCE = 20

    def __init__(self, position):
        super().__init__()
        self.setposition(position)
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        current_position = self.ycor()
        if current_position < 250:
            self.sety(current_position + self.MOVE_DISTANCE)

    def move_down(self):
        current_position = self.ycor()
        if current_position > -230:
            self.sety(current_position - self.MOVE_DISTANCE)
