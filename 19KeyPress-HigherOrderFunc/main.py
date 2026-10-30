from turtle import Screen, Turtle



screen = Screen()
#cursor = Turtle(shape='turtle')

# # 1. Controllable cursor

# #directions
# def move_forward():
#     cursor.forward(10)
# def move_backwards():
#     cursor.backward(10)
# def turn_right():
#     cursor.right(5)
# def turn_left():
#     cursor.left(5)
# #clear
# def clear():
#     cursor.reset()
    
# keys_to_func = {
#     'w' : move_forward , 
#     's' : move_backwards , 
#     'a' : turn_left , 
#     'd' : turn_right , 
#     'c' : clear ,
# }
# # def key_press(keybind):
# #     for key in keys_to_func:
# #         screen.onkey(fun=keys_to_func[key],key=key)

# # key_press(screen.listen)

# screen.onkey(move_forward, 'w')
# screen.onkey(move_backwards, 's')
# screen.onkey(turn_left, 'a')
# screen.onkey(turn_right, 'd')
# screen.onkey(clear, 'c')

# screen.listen()
# screen.exitonclick()

##################
##################

# 2. Turtle Race

import random

colors = [
"Red",
"Orange",
"Yellow",
"Green",
"Blue",
"Indigo",
"Violet"
]

width = 500
height = 400

screen.setup(width, height)
choice = screen.textinput("Turtle Race","Choose a color: ")

competitors = {}

starting_y_axis = -100

for i in range(len(colors)):
    starting_y_axis += (200 / len(colors))
    set_location = ((-width + 250), starting_y_axis)
    competitors[colors[i]] = Turtle(shape='turtle')
    competitors[colors[i]].color(colors[i])
    competitors[colors[i]].penup()
    competitors[colors[i]].goto(x= set_location[0], y =set_location[1])

racing = True

while racing:
    for i in range(len(colors)):
        competitors[colors[i]].forward(random.randint(1,10))
        if competitors[colors[i]].position()[0] >= (width/2) - 30:
            winner = colors[i]
            print(f"Hooray for {winner}!!")
            racing = False
            break

if choice.lower() == winner.lower():
    screen.title("You Won")
else:
    screen.title(f"You Lost. {winner} is at the podium.")

screen.exitonclick()