from random import randint
import os

clear = lambda: os.system('cls')
should_restart = True

logo = """   _____                     _               _   _                 _               
  / ____|                   (_)             | \ | |               | |              
 | |  __ _   _  ___  ___ ___ _ _ __   __ _  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __| | '_ \ / _` | | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \ | | | | (_| | | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/_|_| |_|\__, | |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
                                      __/ |                                        
                                     |___/                                         """

while should_restart:
    
    clear()

    print(logo)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")

    guessing_number = randint(1, 100)
    print(guessing_number)

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard' - ")

    if difficulty == 'easy':
        attemps = 10
    elif difficulty == 'hard':
        attemps = 5
    else:
        exit()

    game_continue = True

    while game_continue:

        print(f"You have {attemps} attempts remaining to guess the number.")
        guess = int(input("Make a guess - "))
            
        if guess > guessing_number:
            print("Too low.")
            attemps -= 1

            if attemps == 0:
                game_continue = False
                print("You definetly loose the game.")

                restart = input("Do you want to restart the game ? 'y' or 'n' - ")

                if restart == 'y':
                    should_restart = True
                else:
                    should_restart = False

        elif guess < guessing_number:
            print("Too high.")
            attemps -= 1

            if attemps == 0:
                game_continue = False
                print("You definetely loose the game.")

                restart = input("Do you want to restart the game ? 'y' or 'n' - ")

                if restart == 'y':
                    should_restart = True
                else:
                    should_restart = False
        else:
            print("You win !")
            game_continue = False
            
            restart = input("Do you want to restart the game ? 'y' or 'n' - ")

            if restart == 'y':
                should_restart = True
            else:
                should_restart = False