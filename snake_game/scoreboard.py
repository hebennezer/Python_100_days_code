from turtle import Turtle

ALIGMENT = "center"
FONT = ("Arial", 20, "normal")
GAME_OVER_FONT = ("Arial", 30, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGMENT, font=GAME_OVER_FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
