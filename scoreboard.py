from turtle import Turtle
Font =('Courier',24,'normal')
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.x=0
        self.pencolor("white")
        self.penup()
        self.goto(-40,260)
        self.pendown()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"score: {self.x}",move = False,font=Font)

    def game_over(self):
        self.goto(-50,0)
        self.write("GAME OVER",move=False,font=Font)

    def scoreboard(self):
        self.x +=1
        self.clear()
        self.update_scoreboard()

