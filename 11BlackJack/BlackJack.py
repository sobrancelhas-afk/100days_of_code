import json
import random
import art

def draw_card(draws, who):
    for draw in range(0,draws):
        x = random.choice(list(card_table))
        who[x] = card_table[x]
        card_table.pop(x)
    if who == player_hand:
        print(list(player_hand.keys()))
    
    return calc_points(x=who)


# Ler arquivo json com lista das cartas
#######################################
with open('11BlackJack/cards.json', 'r') as file:
    cards_json = json.load(file)

card_table = {}
for i in range(0,len(cards_json['cards'])):
    card_table[cards_json['cards'][i]['code']] = cards_json['cards'][i]['points']

print(art.logo)

# Retirar 2 cartas aleatoriamente e #contabilizar pontos
########################################################

player_hand = {}
CPU_hand = {}
player_points = 0
cpu_points = 0

def calc_points(x):
    aces = ['AH','AD','AC','AS']

    if any(card in aces for card in x.keys()): #check if has an Ace
        while sum(x.values()) > 21 and (any(value==11 for value in x.values())):
            for i in aces:
                if (i in x.keys()):
                    x[i] = 1
    return sum(x.values())

def check_winner(player_points, cpu_points):
    if player_points == cpu_points:
        print(f"It's a draw\nYou:{player_points} - CPU: {cpu_points}")
    elif cpu_points > 22:
        if player_points < 22:
            print(f"You Win!\nYou:{player_points} - CPU: {cpu_points}")
        else:
            print(f"It's a draw\nYou:{player_points} - CPU: {cpu_points}")
    elif player_points < 22 and (player_points > cpu_points):
        print(f"You Win!\nYou:{player_points} - CPU: {cpu_points}")
    else:
        print(f"You Lose!\nYou:{player_points} - CPU: {cpu_points}")

def estouro(player_points, cpu_points):
    if (player_points > 21) and (cpu_points > 21):
        print(f"It's a draw\nYou:{player_points} - CPU: {cpu_points}")
        return True
    elif (player_points == 21) and (cpu_points == 21):
        print(f"It's a draw\nYou:{player_points} - CPU: {cpu_points}")
        return True
    elif player_points == 21:
        print(f"You Win!\nYou:{player_points} - CPU: {cpu_points}")
        return True
    elif cpu_points == 21:
        print(f"You Lose!\nYou:{player_points} - CPU: {cpu_points}")
        return True
    elif player_points > 21:
        print(f"You Lose!\nYou:{player_points} - CPU: {cpu_points}")
        return True
    elif cpu_points > 21:
        print(f"You Win!\nYou:{player_points} - CPU: {cpu_points}")
        return True
    else:
        return False

player_points = draw_card(draws=2, who=player_hand)
cpu_points = draw_card(draws=2, who=CPU_hand)

print(f"CPU's first card: {next(iter(CPU_hand))}\n")

# Continuar jogando?
####################

while True:
    print(player_points)

    #Estourou /
    if estouro(player_points, cpu_points):
        break #############TODO CHECAR ISTO

    stop = input("Stop?(y)\n")

    if stop.lower() == "y":
        while cpu_points < 17:
            draw_card(draws=1, who=CPU_hand)
            cpu_points = calc_points(x=CPU_hand)
        check_winner(player_points,cpu_points)
        break

    player_points = draw_card(draws=1, who=player_hand)
    cpu_points = draw_card(draws=1, who=CPU_hand)

    # Critérios de Fim
    ##################    

    