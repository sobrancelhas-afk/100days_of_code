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
roof = Paddle(spawn_coords=(0, +SCREEN_Y), paddle_width= 200)
floor = Paddle(spawn_coords=(0, -SCREEN_Y), paddle_width= 200)

################## TODO
##################
collideable = {
    player.collision_coords : True,
    wall.collision_coords : True,
    roof.collision_coords : True,
    floor.collision_coords : True
}
##################
##################

#Generate Ball
ball = Ball()

#mover paddle Up e Down
screen.onkey(fun=player.move_up,key="w")
screen.onkey(fun=player.move_down,key="s")  

screen.listen()
while game:
    
    sleep(0.005)
    ball.move()
    screen.update()

    #collision with ball
    if ball.just_collided(bumper=player) 
    
    ####  Colocar collision dentro da func de ball ou das outras turtles???

    # if wall.update_collision_body(bumper=ball):
    #     ball.just_collided()

    # if roof.update_collision_body(bumper=ball):
    #     ball.just_collided()

    # if floor.update_collision_body(bumper=ball):
    #     ball.just_collided()
    
screen.exitonclick()