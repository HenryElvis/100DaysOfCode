logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)

def Add(n1, n2):
    return n1 + n2

def Substract(n1, n2):
    return n1 - n2

def Multiply(n1, n2):
    return n1 * n2

def Divide(n1, n2):
    return n1 / n2

calculation = {
    "+": Add,
    "-": Substract,
    "*": Multiply,
    "/": Divide
}

def Calcul():
    f_number = float(input("What's the first number ? - "))

    for i in calculation:
        print(i)

    can_continue = True

    while can_continue:
        symbol = input("Pick an operation from the line above: ")
        s_number = float(input("What's the second number ? - "))

        operation_delegate = calculation[symbol]

        print(f"{f_number} {symbol} {s_number} = {operation_delegate(f_number, s_number)}")

        f_number = operation_delegate(f_number, s_number)

        result = input(f"Type 'y' to continue calculating with {f_number}, 'new' to make new calculation ,or type 'n' to exit - ")

        if result != 'y':
            can_continue = False

            if result == 'new':
                Calcul()

Calcul()