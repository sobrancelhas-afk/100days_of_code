from turtle import Turtle
from random import randint

START_THROW_ANGLE = 30

class Ball(Turtle):

    def __init__(self):
        super().__init__()

        self.color('white')
        self.shape('circle')
        self.setheading(randint(180 - START_THROW_ANGLE, 180 + START_THROW_ANGLE))
        self.speed('slowest')

    def move(self):
        self.forward(2)