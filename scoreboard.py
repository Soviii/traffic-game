from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.goto(-235, 265)
        self.color("white")
        self.writeLevel()
   
    def writeLevel(self):
        self.clear()
        self.write(f"Level {self.level}", align="center", font=("Courier", 20, "normal"))

    def levelIncrease(self):
        self.level += 1
        self.writeLevel()
    
    def gameOver(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=("Courier", 40, "normal"))