water = 300
milk = 2232
coffee = 100
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 150,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 250,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 119,
}

# {
#     "water": f"{water}ml" if water < 1000 else f"{water / 1000:.2f}L",
#     "milk": f"{milk}ml" if milk < 1000 else f"{milk / 1000:.2f}L",
#     "coffee": f"{coffee}g" if coffee < 1000 else f"{coffee / 1000:.2f}Kg",
# }

coins = {
    'quarters': 0, # 0.25,
    'dimes': 0, # 0.10,
    'nickles': 0, # 0.05,
    'pennies': 0, # 0.01
}

def calculate_money(pocket=coins):
    return pocket["quarters"] * 25 + pocket["dimes"] * 10 + pocket["nickles"] * 5 + pocket["pennies"] * 1

def change_coins(due_change = change):
    return_coins = {}
    coin_values = {'quarters':25, 'dimes':10, 'nickles':5, 'pennies':1}
    for coin in coins:
        return_coins[coin] = due_change // coin_values[coin]
        due_change -= return_coins[coin] * coin_values[coin]
    return return_coins
        


# 1 Manter em "machine_on" com a pergunta em tela sempre que nao esta em atendendimento
machine_on = True
#while machine_on:
while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    # 2. Quando a palavra 'off' é escrita, a máquina desliga.
    if choice == 'off':
        machine_on = False
        break

    # 3. Quando a palavra 'report' é escrita, são exibidos os "resources"
                # Water: 100ml
                # Milk: 50ml
                # Coffee: 76g
                # Money: $2.5
    if choice == 'report':
        for i in resources:
            print(f"{i}: {resources[i]}")
        print(f"""money: ${calculate_money() / 100:.2f}""")
        continue

    # 4. a) checa se tem 'resources' suficientes pra servir a 'choice'
            # b) mensagem: “Sorry there is not enough {resource}.”
    enough_resources = True
    if choice in MENU:
        for i in MENU[choice]['ingredients']:
            if resources[i] < MENU[choice]['ingredients'][i]:
                enough_resources = False
                print(f"Sorry there is not enough {i} in the machine.")
                continue            
    # 5. 5. Process coins.
            # a. Se 'resources' suficientes, then ask to insert coins.
            # b. quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
            # c. Calcular total inserido
    if enough_resources == True:
        print("Insert coins: \n")
        last_inserted = {}
        for cointype in coins:
            last_inserted[cointype] = int(input(f"{cointype}: "))      
    else:
        continue

    # TODO 6. Check transaction successful?
    # a. Se valor inserido insuficiente dizer “Sorry that's not enough money. Money refunded.”.
    if calculate_money(last_inserted) <  MENU[choice]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        continue
     # b. Se valor suficiente, Custo da bebida soma ao 'profit/money', que é exibido ao digitar “report”.

    for cointype in coins:
        coins[cointype] += last_inserted[cointype]
# c. A máquina deve devolver troco.
    # check_change
    if calculate_money(last_inserted) > MENU[choice]['cost']:
        change = calculate_money(last_inserted) - MENU[choice]['cost']
        print(f"Your due change is ${change / 100}")

        # calcular moedas a descontar para troco, a começar pelas de maior valor
        
        # if calculate_money() < change:
        #     print("There is not enough change money. Money refunded.") 
        #     for cointype in coins:
        #             coins[cointype] -= last_inserted[cointype]
        # else:
        coins_to_return = change_coins()
        for coin in coins:
            # TODO validação de Troco
            coins[coin] -= coins_to_return[coin]
            print(f"{coins_to_return[coin]} {coin} returned.")        
        
# 7. Make Coffee.
        # a. Deduzir os ingredientes usados na bebida de 'resources'
        for i in MENU[choice]['ingredients']:
            resources[i] -= MENU[choice]['ingredients'][i]

        # b. Após dedução exibir: “Here is your ____. Enjoy!”.
        print(f"Here is your {choice}. Enjoy!")