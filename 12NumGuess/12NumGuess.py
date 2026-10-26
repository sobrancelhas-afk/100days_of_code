import random
import art

lower_range = 1
upper_range = 100

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 0 : easy or 1 : hard.\n")

    while difficulty not in ["0", "1"]:
        print("Incorrect Input.")
        return set_difficulty()
    #escrita elegante, mas sujeita ao problema de abrir instância dentro de instância (StackOverflow)
    
    return int([10 if difficulty == "0" else 5][0])

def check_guess(remaining_attempts):

    guess = int(input(f"You have {remaining_attempts} attempts remaining to guess the number.\nMake a guess: "))
    
    remaining_attempts -= 1

    if guess != goal:
        print(["\nToo high.\n" if (guess > goal) else "\nToo low.\n"][0])

        if remaining_attempts == 0:
            return print(f"You Lost.\nThe correct number was {goal}.")

        check_guess(remaining_attempts)
        return
    
    if guess == goal:
        return print("You Win!")


print(art.logo)
print(f"""Welcome to the Number Guessing Game!\n
I'm thinking of a number between {lower_range} and {upper_range}.""")

goal = random.randint(lower_range,upper_range)

### Check guess
check_guess(set_difficulty())


