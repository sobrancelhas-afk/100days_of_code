from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

latte = MenuItem(name = "latte", cost = 2.5, water = 200, coffee = 24, milk = 150)
cappuccino = MenuItem(name = "cappuccino", cost = 3,water = 250, milk = 100, coffee =24)
espresso = MenuItem(name = "espresso", cost = 1.5,water = 50, milk = 0, coffee =18)

MenuObj = Menu()
cardapio = MenuObj.get_items().split(sep='/')[:-1]

cafeteira = CoffeeMaker()

cashier = MoneyMachine()

machine_on = True
#cafeteira.report()
while machine_on:
    print("\nChoose from the Menu:\n")
    print(*cardapio, sep="\n")

    choice = input()

    if choice == 'report':
        cashier.report()
        continue

    if choice == 'off':
        print('turning off...\n')
        machine_on = False
        break

    choice = MenuObj.find_drink(choice)

    if not cafeteira.is_resource_sufficient(choice):
        print("Insufficient resources to make that!\n")
        continue
    else:
        if not cashier.make_payment(choice.cost):
            print("Insufficient funds!\n")
            continue
        else:
            cafeteira.make_coffee(choice)




