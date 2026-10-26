import game_data
import art
import random

# Visualizar o formato dos dados
# print(db[0]) # variáveis de cada dict -> name, follower_count, description, country
# print (len(db)) # lista de 50 entradas (dicts)
# Iniciar loop do jogo
# Ler base de dados
db = game_data.data

score = 0

while len(db) > 0:

    # Ler base de dados
    db = game_data.data
    # Determinar pontuação inicial = 0,
    print(art.logo)

    #Escolher primeiro comparador (a)
    a = random.choice(db)

#Puxar comparação (b) removendo (a) da base
    db.remove(a)
    b = random.choice(db)

    #dar a opção de adivinhar o que tem maior follower_count

    choice = input(f"""Which has more followers?:\n
{a['name']}, a {a['description']} from {a['country']}\n
{art.vs}\n
{b['name']}, a {b['description']} from {b['country']}\n
Type 1 or 2: """)

    while choice not in ("1","2"):
        choice = input("There was something wrong with the input.\nType 1 or 2:")

    a_followers = int(a['follower_count'])
    b_followers = int(b['follower_count'])

    # se acertar, acumula placar
    if (choice == '1') and (
        a_followers >= b_followers
        ) or (choice == '2') and(
        a_followers <= b_followers
        ):
        # o comparado (b) toma a posição de (a) antes do loop
        a = b
        score += 1
        print(f"{art.win}\nCurrent Score: {score}")
    # se errar, zera e começa de novo
    else:
        score = 0
        print(f"""
{art.fail}\nIncorrect Choice! Your Score has been reset.\n
{a['name']} : {a_followers} | {b['name']} : {b_followers}\n
Restarting the game...""")
        

print("Incredible... There are no candidates left!")