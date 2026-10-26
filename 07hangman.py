import random

lifes = 5
guessed = []
word_list = ['pano', 'bala', 'fio']
word = random.choice(word_list)
end = False

print(f"Game Start\nlifes: {lifes}\n")
print("".join(["_ " for char in word]))  

def game():
  while end == False:
    char_check()
def end_game():
  global lifes
  global guessed
  global word
  global end

  if lifes == 0:
    print("You lose")
    end = True
  elif set(word).issubset(set(guessed)):
    print("You win")
    end = True
  

def char_check():
  
  global guessed
  global word
  global lifes
  current_guess = input("Choose a letter: \n")
  if current_guess in guessed:
    print("Character already attempted, pick another!")
    
  else:
    guessed.append(current_guess)
    #list comprehension+.join is faster/cleaner than std for loop
    word_concealed = " ".join(["_" if char not in guessed else char for char in word])
    print(word_concealed)  
    if current_guess not in word:
      lifes -= 1
      print("Wrong")
    else:
      print("Right")
      
    print(f'There are {lifes} lives left')
  end_game()

game()