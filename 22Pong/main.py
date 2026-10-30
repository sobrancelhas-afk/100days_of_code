from turtle import Turtle, Screen
from time import sleep

from paddle import SCREEN_X, SCREEN_Y,Paddle
from ball import Ball

screen = Screen()
screen.setup(width=2*SCREEN_X, height=2*SCREEN_Y)
screen.screensize(canvwidth=SCREEN_X, canvheight=SCREEN_Y)
screen.bgcolor("black")
screen.title("POOOOONG")
#turn off tracer to make it less laggy and .update() manually in code
screen.tracer(0)
screen.delay(0)

## TODO Create paddles


## TODO Create ball

## TODO Create ScoreBoard

## Game Loop


game = True
player = Paddle()
ball = Ball()

#mover paddle Up e Down
screen.onkey(fun=player.move_up,key="w")
screen.onkey(fun=player.move_down,key="s")  

screen.listen()
while game:

    player.move()
    ball.move()
    screen.update()

    #collision with ball
    ###

    sleep(0.005)
screen.exitonclick()