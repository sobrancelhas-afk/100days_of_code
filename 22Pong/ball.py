from turtle import Turtle
from random import randint


class Ball(Turtle):

    def __init__(self, last_collision = None):
        super().__init__()

        self.color('white')
        self.shape('circle')
        self.setheading(randint(180 - 30, 180 + 30))
        self.speed('slowest')

        self.last_collision = last_collision
        self.direction_x = 1
        self.direction_y = 1 if self.heading() < 180 else -1

    def move(self):

        if self.direction_y > 0:
            self.forward(2 * self.direction_y)
        else:
            self.forward(-2 * self.direction_y)
        #########################################
        if self.direction_x > 0:
            self.forward(2 * self.direction_x)
        else:
            self.forward(-2 * self.direction_x)

    def just_collided(self, bumpers):

        ###### X_AXIS COLLISION
        # if collision on X axis

        self.direction_x = -1 * self.direction_x

        if  self.direction_x == 1:
            self.setheading(randint(180 - 30, 180 + 30))
        else:
            self.setheading(randint(360 - 30, 360 + 30))

        ###### Y_AXIS COLLISION
        # if collision on Y axis        
        
        self.direction_y = -1 * self.direction_y

        if  self.direction_y == 1:
            self.setheading(randint(270 - 30, 270 + 30))
        else:
            self.setheading(randint(90 - 30, 90 + 30))

        ### Receive all collision coords??????? TODO
        ### KEEP collision coords check in paddle or in ball?

        for collision in self.collision_coords:
            if abs(self.xcor() - collision[0]) < 20 and abs(self.ycor() - collision[1]) < 20:
                self.collidable = False
                return True