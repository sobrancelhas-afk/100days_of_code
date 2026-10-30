from turtle import Turtle

SCREEN_X = 700
SCREEN_Y = 250

class Paddle(Turtle):
    def __init__(self):
        super().__init__()

        self.paddle_parts = []
        self.paddle_parts_coords = []
        self.paddle_size = 6

        for n in range(self.paddle_size):
            part = self.generate_paddle_part(part_n=n)
            self.paddle_parts.append(part)

        self.core = self.paddle_parts[0]
        
        #generate entire paddle
    def generate_paddle_part(self,part_n):
        paddle = Turtle(shape='square')
        paddle.teleport(-SCREEN_X + 100, self.paddle_size+(part_n*20))
        paddle.color('white')
        paddle.setheading(90)  
        paddle.penup()
        paddle.speed(0)
        self.paddle_parts_coords.append(paddle.pos())
        return paddle            

    def move(self):

        for n in range(self.paddle_size):
            x_cor= self.core.xcor()
            y_cor= self.core.ycor() + (n * 20)
            self.paddle_parts[n].goto(x_cor,y_cor)
            

    def move_up(self):
        self.core.forward(20)
    def move_down(self):
        self.core.backward(20)