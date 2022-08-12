from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
paiement = MoneyMachine()
menu = Menu()

machine_off = False

while not machine_off:
    choice = input(f"What would you like? {menu.get_items()}:")

    if choice == "report":
        coffee_machine.report()
    elif choice == "latte" or choice == "cappuccino" or choice == "espresso":
        drink = menu.find_drink(choice)
        if coffee_machine.is_resource_sufficient(drink):
            if paiement.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
        else:
            print("Cannot make this coffee")
    elif choice == "off":
        machine_off = True
