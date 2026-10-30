from random import randint
from turtle import Turtle

SCREEN_X = 300
SCREEN_Y = 300

DEFAULT_SCREEN = (SCREEN_X, SCREEN_Y)
BORDER_SPAWN_OFFSET = 75

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5)
        self.color('yellow')
        #self.respawn()
        
    ## TODO the respawn coords don't avoid the snake's body, only it's tail

    def respawn(self):
        self.teleport(
                    randint(-DEFAULT_SCREEN[0]+BORDER_SPAWN_OFFSET, DEFAULT_SCREEN[0]-BORDER_SPAWN_OFFSET),
                    randint(-DEFAULT_SCREEN[1]+BORDER_SPAWN_OFFSET, DEFAULT_SCREEN[1]-BORDER_SPAWN_OFFSET)
                    )