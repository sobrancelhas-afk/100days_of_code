from turtle import Turtle

SCREEN_X = 700
SCREEN_Y = 350
PADDLE_OFFSET = 100


starting_player_coords = (-SCREEN_X + PADDLE_OFFSET, 0)

class Paddle(Turtle):
    def __init__(self,can_reverse_ball_trajectory = True, spawn_coords = starting_player_coords, paddle_length = 6, paddle_width = 1):
        super().__init__()

        self.spawn_coords = spawn_coords
        self.paddle_width = paddle_width
        self.paddle_length = paddle_length

        self.can_reverse_ball_trajectory = can_reverse_ball_trajectory

        self.generate_paddle()
        self.collision_body()

        #generate entire paddle
    def generate_paddle(self):
        self.shape('square')
        self.shapesize(stretch_len=self.paddle_length, stretch_wid=self.paddle_width) # < -----
        self.teleport(self.spawn_coords[0], self.spawn_coords[1]) #< ----
        self.color('white')
        self.setheading(90)  
        self.penup()
        self.speed(0)

    def move_up(self):
        self.forward(20)
        self.collision_body()
    def move_down(self):
        self.backward(20)
        self.collision_body()

    def collision_body(self):

        px = self.xcor()
        py = self.ycor()

        self.paddle_edge_left = px - (self.paddle_width * 20/2)
        self.paddle_edge_right = px + (self.paddle_width* 20/2)
        self.paddle_edge_bottom = py - (self.paddle_length* 20/2)
        self.paddle_edge_top = py + (self.paddle_length* 20/2)


