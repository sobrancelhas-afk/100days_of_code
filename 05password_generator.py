import random

letters= ['a', 'b', 'c', 'd']
numbers = ['0','1','2','3','4']
symbols = ['!','@','#','$']

ll = len(letters)
ln = len(numbers)
ls = len(symbols)

rl = random.randint(0,ll-1)
rn = random.randint(0,ln-1)
rs = random.randint(0,ls-1)

pwselect = []
pwselect.extend(letters + numbers + symbols)

pwlen = 8
letcount = 3
numcount = 2
symcount = 3

finalpw = ''

for i in range(0,letcount):
  finalpw += random.choice(letters)
for i in range(0,numcount):
  finalpw += random.choice(numbers)
for i in range(0,symcount):
  finalpw += random.choice(symbols)
  
finalpw = ''.join(random.sample(finalpw,len(finalpw)))

print(f'{finalpw}\n')