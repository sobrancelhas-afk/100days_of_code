import random

rps=['✊','🖐️','✌️']

a = int(input('rock (0), paper (1) or scissors (2)?\n'))
b = random.randint(0,2)

default_print = f'YOU:\n{rps[a]}\nCPU:\n{rps[b]}\n'


if a == b:
  result = f'{default_print}IT IS A TIE!'
elif a == 0:
  if b == 1:
    result =  f'{default_print}YOU LOSE!'
  else:
    result =  f'{default_print}YOU WIN!'
elif a == 1:
  if b == 2:
    result =  f'{default_print}YOU LOSE!'
  else:
    result =  f'{default_print}YOU WIN!'
else: # a == 2
  if b == 0:
    result =  f'{default_print}YOU LOSE!'
  else:
    result =  f'{default_print}YOU WIN!'


print(result)