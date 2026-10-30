from time import sleep
from turtle import Screen

from food import SCREEN_X, SCREEN_Y, Food
from scoreboard import ScoreBoard
from snake import Snake

SLEEP_TIME = 0.07
BORDER_OFFSET = -20

screen = Screen()
screen.setup(SCREEN_X*2, SCREEN_Y*2)
screen.screensize(SCREEN_X, SCREEN_Y)
screen.bgcolor('black')
screen.title('SNAAAAkeeee')
screen.tracer(0)

game = True


food = Food()
snake = Snake()
snake.generate_snake()
scoreboard = ScoreBoard()

screen.onkey(fun=snake.left, key='a')
screen.onkey(fun=snake.right, key='d')
screen.onkey(fun=snake.down, key='s')
screen.onkey(fun=snake.up, key='w')

screen.listen()
while game:

    sleep(SLEEP_TIME)
    snake.move()
    screen.update() 
    
    # Detect food collision
    if snake.head.distance(food) < 20:
        food.respawn()
        snake.snake_size += 1
        snake.generate_snake()
        scoreboard.update_score()

    # Detect wall collision
    if (
        snake.head.xcor() < (-SCREEN_X -BORDER_OFFSET) 
        or snake.head.ycor() < (-SCREEN_Y -BORDER_OFFSET)
        or snake.head.xcor() > (SCREEN_X +BORDER_OFFSET) 
        or snake.head.ycor() > (SCREEN_Y +BORDER_OFFSET)
        ):
        scoreboard.game_over()
        game = False

    #Detect body collisions
    for coord in snake.collisions_body[1:]:
        if snake.head.distance(coord) < 10:
            scoreboard.game_over()
            game = False

screen.exitonclick()