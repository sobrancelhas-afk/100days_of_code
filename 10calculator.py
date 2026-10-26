###Capitalize first letter###
#############################
def format_name(f_name='mAdEr', l_name='cluCkEr'):
    full_name = [f_name, l_name]
    return list(map(lambda x:x[0].upper()+x.lower()[1:], full_name))

eita, eita2 = format_name()

#print(''.join([eita, ' ', eita2]))

#############################
#############################

# help
# i 
# need 
# to 
# rember
# how to 
# Docstring multiline comment:
# Ctrl + /
 
#############################
#############################

import os
import sys

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations={
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

print('''
##########################
######THE CALCULATOR######
##########################
    '''
)
def calculator():

    x = float(input('Welcome to the Calculator\nChoose the first number:\n'))
   
    while True: 
        for item in operations:
            print(item)   
        z = input('Pick the operation:\n')
        y = float(input('Second number\n'))
        x = operations[z](x, y)
        repeat = (
            input(f"{x} {z} {y} = {x}\nPress y to continue calculating with {x}\n"))
        if repeat.lower() != 'y':
            python = sys.executable
            os.execl(python, python, *sys.argv)
                    
calculator()