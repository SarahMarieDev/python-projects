from turtle import Turtle


class Scoreboard(Turtle):
    
    ALIGNMENT = "center"
    FONT = ('Courier', 24, 'normal')
    HIGH_SCORE = open("data.txt", mode="r").read()
    

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(self.HIGH_SCORE)
        self.penup()
        self.pencolor("white")
        self.hideturtle()
        self.setposition(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=self.ALIGNMENT, font=self.FONT)
        
    def reset(self):
        self.HIGH_SCORE = open("data.txt", mode="w").write(str(self.high_score))
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        
