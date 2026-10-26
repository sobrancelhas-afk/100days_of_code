water = 300
milk = 2232
coffee = 100
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
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
    return coins["quarters"] * 0.25 + coins["dimes"] * 0.1 + coins["nickles"] * 0.5 + coins["pennies"] * 0.01

# TODO. 1 Manter em "machine_on" com a pergunta em tela sempre que nao esta em atendendimento
machine_on = True
#while machine_on:
choice = input("What would you like? (espresso/latte/cappuccino): ")

# TODO 2. Quando a palavra 'off' é escrita, a máquina desliga.
if choice == 'off':
    machine_on = False

# TODO 3. Quando a palavra 'report' é escrita, são exibidos os "resources"
            # Water: 100ml
            # Milk: 50ml
            # Coffee: 76g
            # Money: $2.5
if choice == 'report':
    for i in resources:
        print(f"{i}: {resources[i]}")
    print(f"""money: ${calculate_money():.2f}""")

# TODO 4. a) checa se tem 'resources' suficientes pra servir a 'choice'
        # b) mensagem: “Sorry there is not enough {resource}.”
enough_resources = True
if choice in MENU:
    for i in MENU[choice]['ingredients']:
        if resources[i] < MENU[choice]['ingredients'][i]:
            enough_resources = False
            print(f"Sorry there is not enough {i} in the machine.")

# TODO 5. 5. Process coins.
        # a. Se 'resources' suficientes, then ask to insert coins.
        # b. quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
        # c. Calcular total inserido
if enough_resources == True:
    print("Insert coins: \n")
    last_inserted = {}
    for cointype in coins:
        last_inserted[cointype] = int(input(f"{cointype}: "))      

# TODO 6. Check transaction successful?
        # a. Se valor inserido insuficciente dizer “Sorry that's not enough money. Money refunded.”.
if calculate_money(last_inserted) <  MENU[choice]['cost']:
    print("Sorry that's not enough money. Money refunded.")
        # b. Se valor suficiente, Custo da bebida soma ao 'profit/money', que é exibido ao digitar “report”.
    else:
        for cointype in coins:
            coins[cointype] += last_inserted[cointype]
        # c. A máquina deve devolver troco. Arredondado a 2 casas decimais
        # check_change
        if calculate_money(last_inserted) > MENU[choice]['cost']:
            change = calculate_money(last_inserted) - MENU[choice]['cost']
            print(f"You have ${change} change")

            #contar $ cheio


# TODO 7. Make Coffee.
        # a. Deduzir os ingredientes usados na bebida de 'resources'
        # b. Após dedução exibir: “Here is your ____. Enjoy!”.