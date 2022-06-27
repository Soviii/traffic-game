from turtle import Turtle

MOVEDISTANCE = 7

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.goto(0,-200)
    
    def moveForward(self):
        self.forward(MOVEDISTANCE)

    def moveBackward(self):
        self.backward(MOVEDISTANCE)
    
    def reposition(self):
        self.goto(0,-200)
    
    def collision(self, traffic):
        for npc in traffic:
            if self.distance(npc) < 22:
                return True
        return False