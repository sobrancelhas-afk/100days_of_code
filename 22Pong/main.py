from turtle import Screen
from time import sleep

from paddle import Paddle, SCREEN_X, SCREEN_Y, PADDLE_OFFSET
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

game = True

#Generate collideables
player = Paddle()
wall = Paddle(spawn_coords=(+SCREEN_X - PADDLE_OFFSET, 0), paddle_length=50)
roof = Paddle(spawn_coords=(0, +SCREEN_Y), can_reverse_ball_trajectory=False, paddle_length =1, paddle_width= 200)
floor = Paddle(spawn_coords=(0, -SCREEN_Y), can_reverse_ball_trajectory=False, paddle_length =1, paddle_width= 200)

################## TODO
##################
collideables = [
    player,
    wall,
    roof,
    floor
]
##################
##################

#Generate Ball
ball = Ball(collideables=collideables)

#mover paddle Up e Down
screen.onkey(fun=player.move_up,key="w")
screen.onkey(fun=player.move_down,key="s")  

screen.listen()
while game:
    
    sleep(0.003)
    ball.move()
    screen.update()

    #collision with ball
    ball.just_collided(bumper=player) 
    ball.just_collided(bumper=wall)
    ball.just_collided(bumper=floor)
    ball.just_collided(bumper=roof)
    
screen.exitonclick()