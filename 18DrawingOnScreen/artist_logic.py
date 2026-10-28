from turtle import Screen, Turtle, screensize
import random

cursor = Turtle()
Screen().colormode(255)

class Artist:
    def __init__(self, palette):
        self.palette = palette

    def draw_dot(self, width = 12):
        #Sett random color from palette
        rand_col = random.choice(self.palette)
        cursor.pencolor(rand_col)
        #Desenhar ponto
        cursor.dot(width)

    def draw(self, res=(400,300),dots_per_line = 5, dots_per_column = 5):

        cursor.speed("fastest")
        #Define screen size or leave blank for default
        screensize(res[0], res[1])

        #define starting point and ending (screen ranges from -x,-y : x, y)
        start = (-res[0],-res[1])

        #Initialize cursor's position()
        cursor.teleport(start[0],start[1]) #move it from standard center to the corner of the screen
        # cursor.setheading(0) # turn the cursor's angle to face it's path
        
        #define distance among the dots -> must multiply by 2 (screen ranges from -x,-y : x, y)
        distance_dpl = int(2 * res[0] / ( 1 + dots_per_line))  #+1 to adjust with center

        distance_dpc = int(2 * res[1] / ( 1 + dots_per_column)) 

        # walk
        cursor.penup() # turn off default line tracing

        c_dot_num, l_dot_num = 0, 0 # counter for point n drawn in line or column

        while l_dot_num < dots_per_column: #while doesnt reach limit of y axis
            
            c_dot_num = 0
            # reset x axis position to 0, and add distance per dots do y axis
            cursor.teleport(x = start[0], y = cursor.position()[1] + distance_dpc)
            l_dot_num += 1   

            while c_dot_num < dots_per_line: # while didnt reach limit of x axis
                c_dot_num += 1                
                cursor.forward(distance_dpl) # walk distance until point
                self.draw_dot()

        cursor.teleport(0,0)