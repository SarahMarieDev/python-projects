from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.pencolor("black")
        self.penup()
        self.hideturtle()
        self.setposition(-280, 260)
        self.update_scoreboard()

    
    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_score(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()
        

    def game_over(self):
        self.setposition(0,0)
        self.write("GAME OVER", align="center", font=FONT)
        




