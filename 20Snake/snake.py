from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake_size = 3
        self.collisions_body = []
        
        self.entire_body = []

        for n in range(self.snake_size):
            self.entire_body.append(self.generate_snake_segment())
            self.collisions_body.append(self.entire_body[n].pos())

    def generate_snake_segment(self, turt_shape='square',turt_color='white'):

        multiplier = len(self.entire_body)

        snake_segment = Turtle(shape='square')
        snake_segment.teleport(multiplier * -1000, 0)
        snake_segment.penup()
        snake_segment.color('white')

        self.collisions_body.append(snake_segment.pos())

        return snake_segment

    def generate_snake(self):

        self.entire_body.append(self.generate_snake_segment())
        self.head = self.entire_body[0]

    def move(self):

        self.head.forward(20)

        for segment_num in range(len(self.entire_body)-1, 0,-1):
            coord = self.entire_body[segment_num-1].pos() ## PONTO DE DEBUG -1
            # make body segments move
            self.entire_body[segment_num].goto(coord)
            #register list of body segment coords for collision
            self.collisions_body[segment_num-1] = coord

    

    # change head's facing angle, impede reversal movement
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)