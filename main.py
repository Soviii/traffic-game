import turtle as t
from player import Player
from npc import NPC
import time
from scoreboard import Scoreboard
import random

def nextLevel():
    player.reposition()
    for npc in traffic:
        npc.goto(350,350)
    traffic.clear()
    scoreboard.levelIncrease()

screen = t.Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
traffic = []

difficulty = screen.textinput(title="", prompt="Which difficulty would you like to play on? (easy, medium, or hard)")
while difficulty.lower() not in ["easy", "medium", "hard"]:
    difficulty = screen.textinput(title="", prompt="Error: not a valid difficulty. Enter easy, medium, or hard")
difficulty = difficulty.lower()

screen.listen()
screen.onkey(player.moveForward, "Up")
screen.onkey(player.moveBackward, "Down")

while True:
    createChance = random.randint(1,6)

    if createChance == 1:
        npc = NPC()
        traffic.append(npc)
    
    for npc in traffic:
        npc.moveForward(difficulty)

    if player.ycor() >= 240:
        nextLevel()
    
    if player.collision(traffic):
        scoreboard.gameOver()
        break

    time.sleep(0.1)
    screen.update()
    
screen.exitonclick()

