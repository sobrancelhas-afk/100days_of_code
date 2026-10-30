from turtle import Screen, Turtle, screensize
import random

def random_rgb():
    return random.choice(range(1,256)), random.choice(range(1,256)), random.choice(range(1,256))

# cursor = Turtle()
# Screen().colormode(255)
# cursor.pensize(2)

### 1. Shapes exercise
# for sides in range(3,10):
#     r,g,b = random_rgb()
#     cursor.pencolor(r,g,b)
#     for side in range(sides):
#         cursor.forward(100)
#         cursor.right(360/sides)

### 2. Random Walk Challenge


#andar infinitamente
# speed_algo = 1

# while True:
#     #ocultar turtle
#     cursor.hideturtle()
#     # random angle -> N,S,L,O
#     angle = random.choice([0,90,180,270])
#     # random pencolor
#     r,g,b = random_rgb()
#     cursor.pencolor(r,g,b)
#     # walk
#     cursor.setheading(angle)
#     cursor.forward(20)
#     # Speed
#     cursor.speed(speed_algo)
#     # speed_algo = [10**i for i in range(10, 1)]
#     speed_algo = speed_algo + (7 - speed_algo) * 0.02
#     print(cursor.speed())


### 3. Circle Challenge
# cursor.speed(0)
# c_loops = 66

# for _ in range(c_loops):
#     r,g,b = random_rgb()
#     cursor.pencolor(r,g,b)
#     cursor.circle(100)
#     cursor.right(360 / c_loops)



### 4. Contemporary art
import colorgram
from artist_logic import Artist


# Defining Color Palette
def define_color_palette(palette_color_count = 5):
    palette_profile = colorgram.extract('18DrawingOnScreen/kOn.jpg', palette_color_count)
    palette_rgb_tuple=[]
    for color in palette_profile:
        color_tuple = (color.rgb.r,color.rgb.g,color.rgb.b)
        palette_rgb_tuple.append(color_tuple)
    return palette_rgb_tuple


artoaista = Artist(define_color_palette())
artoaista.draw(dots_per_line = 15, dots_per_column = 15)

screen = Screen().exitonclick()

