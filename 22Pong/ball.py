from turtle import Turtle
from random import randint,choice



class Ball(Turtle):

    def __init__(self, collideables):
        super().__init__()

        self.color('white')
        self.shape('circle')
        self.setheading(randint(180 - 30, 180 + 30))
        self.speed('fast')
        self.movespeed = 1

        self.bumpers = {}
        for collideable in collideables:
            self.bumpers.update({collideable: True})

        self.direction_x = -1
        self.direction_y = 1 if self.heading() < 180 else -1



    def move(self):

        if self.direction_y == 1:
            self.forward(self.movespeed * self.direction_y)
        else:
            self.forward(-self.movespeed * self.direction_y)

        #########################################

        if self.direction_x == 1:
            self.forward(self.movespeed * self.direction_x)
        else:
            self.forward(-self.movespeed * self.direction_x)

    def can_rebound(self, object):

        for bumper in self.bumpers:

            if bumper != object:
                self.bumpers[bumper] = True

        if (object.paddle_edge_left < self.xcor() < object.paddle_edge_right) and (
            object.paddle_edge_bottom < self.ycor() < object.paddle_edge_top):
            self.bumpers[object] = False
            return True

    def just_collided(self, bumper):

        if self.can_rebound(object=bumper):

            ###### X_AXIS COLLISION
            if bumper.can_reverse_ball_trajectory:
                

                if self.direction_x == 1:
                    if self.direction_y == 1:
                        self.setheading(randint(0+30, 90-30))
                    else:
                        self.setheading(randint(180+30, 270-30))   
                else:
                    if self.direction_y == 1:
                        self.setheading(randint(90+30, 180-30))
                        
                    else:
                        self.setheading(randint(90+30, 180-30))

                self.direction_x *= -1
                self.direction_y *= -1
                          
                        
                
                

            ###### Y_AXIS COLLISION
            # if collision on Y axis        
            
            self.direction_y = -1 * self.direction_y


            if self.direction_x == 1:
                if self.direction_y == 1:
                    self.setheading(randint(270 + 30, 360 - 30))               
                else:
                    self.setheading(randint(0 + 30, 90 - 30))
            else:    
                if  self.direction_y == 1:
                    self.setheading(randint(180 + 30, 270 - 30)) 
                    
                else:
                    self.setheading(randint(90 + 30, 180 - 30))
                    


            