from turtle import Turtle

SCREEN_X = 700
SCREEN_Y = 350
PADDLE_OFFSET = 100


starting_player_coords = (-SCREEN_X + PADDLE_OFFSET, 0)

class Paddle(Turtle):
    def __init__(self, spawn_coords = starting_player_coords, paddle_length = 6, paddle_width = 1):
        super().__init__()

        self.spawn_coords = spawn_coords
        self.paddle_width = paddle_width
        self.paddle_length = paddle_length
        #self.shapesize(stretch_len=self.paddle_length, stretch_wid=paddle_width)

        self.generate_paddle()
        self.collision_coords = []
        self.generate_collision_body()

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
    def move_down(self):
        self.backward(20)

    def generate_collision_body(self, bumper):
        #### x axis collisions
        for i in range((-int(self.paddle_length/2)), int(self.paddle_length/2)):
            self.collision_coords.append([self.xcor(), self.ycor() + (i * 20)])

        for i in range((-int(self.paddle_width/2)), int(self.paddle_width/2)):
            self.collision_coords.append([self.xcor() + (i * 20), self.ycor()])

    def update_collision_body(self):
        #update collision_body
        for i in range((-int(self.paddle_length/2)), int(self.paddle_length/2)):
                self.collision_coords[i][0] = (self.xcor() + (i * 20))
        for i in range((-int(self.paddle_width/2)), int(self.paddle_width/2)):
                self.collision_coords[i][1] = (self.ycor() + (i * 20))

        ### Receive all collision coords??????? TODO
        ### KEEP collision coords check in paddle or in ball?

        for collision in self.collision_coords:
            if abs(self.xcor() - collision[0]) < 20 and abs(self.ycor() - collision[1]) < 20:
                self.collidable = False
                return True