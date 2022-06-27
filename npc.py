from turtle import Turtle
import random
STARTING_MOVING_DISTANCE = 5
MOVE_INCREMENT = 5
COLORS = ["red", "lightblue", "yellow", "green", "purple", "pink", "orange"]

class NPC(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2) 
        self.setheading(180)
        self.goto(240, random.randint(-200, 200))
        
    def moveForward(self, difficulty):
        if difficulty == "easy":
            self.forward(STARTING_MOVING_DISTANCE)
        elif difficulty == "medium":
            self.forward(STARTING_MOVING_DISTANCE + MOVE_INCREMENT)
        elif difficulty == "hard":
            self.forward(STARTING_MOVING_DISTANCE + (MOVE_INCREMENT*2))
    
