MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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
    "coffee": 100,
}

TURN_OFF_KEY = "off"
REPORT = "report"

coffee_machine_works = True
money_in_machine = 0

def checking_ressource(coffee):

    for i in resources:
        if resources[i] < MENU[coffee]["ingredients"][i]:
            return False
        else:
            return True

def calculate_price(q, d, n, p, coffee):
    q *= 0.25
    d *= 0.10
    n *= 0.05
    p *= 0.01

    total = q + d + n + p
    coffee_price = MENU[coffee]["cost"]

    if coffee_price > total:
        return f"Sorry that's not enough money. You need to pay {coffee_price}. Money refunded."
    else:
        global money_in_machine
        money_in_machine += coffee_price
        rest = round(total - coffee_price, 2)
        reduice_resources(coffee=coffee)
        return f"Here is ${rest} in change.\nHere is your latte ☕️. Enjoy!"

def reduice_resources(coffee):
    for r in resources:
        resources[r] -= MENU[coffee]["ingredients"][r]
    
while coffee_machine_works:
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ")

    if coffee_type == TURN_OFF_KEY:
        coffee_machine_works = False
        break
    
    if coffee_type == REPORT:
        for i in resources:
            print(f"{i.capitalize()}: {resources[i]}")
        if money_in_machine > 0:
            print(f"Money: ${money_in_machine}")
    elif coffee_type != "espresso" and coffee_type != "latte" and coffee_type != "cappuccino":
        print("Wrong choice ! Select right choice please.")
    else:
        if checking_ressource(coffee_type):
            print("Please insert coin !")
            quarter = int(input("How many quarter ? - "))
            dimes = int(input("How many dimes ? - "))
            nickles = int(input("How many nickles ? - "))
            pennies = int(input("How many pennies ? - "))
            print(calculate_price(q=quarter, d=dimes, n=nickles, p=pennies, coffee=coffee_type))
        else:
            print("Sorry there is not enough resources for this coffee.")