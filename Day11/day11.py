from calendar import c
from random import randint
import os

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

play = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(card):
    index = randint(0, len(cards) -1)

    if index == 0:
        if sum(card) + 11 > 21:
            return 1

    return cards[index]

def sum_score(array):

    sum_array = sum(array)

    if sum_array > 21:
        if 11 in array:
            array.remove(11)
            array.append(1)

    return sum(array)

def has_blackjack(array):
    if len(array) != 2:
        return False
    
    if 10 in array and 11 in array:
        return True

def condition_game(score_player, score_computer):

    if score_player > 21:
        print("You loose")
    else:
        if score_computer < 21:
            if score_player < score_computer:
                print("You loose")
            elif score_player > score_computer:
                print("You win")
            else:
                print("Draw")
        else:
            print("You win")

while play:

    player_card = []
    computer_card = []
    player_score = 0
    computer_score = 0
    can_hand = True
    game_continue = True

    if input("Do you want to play a game of Blackjack ? Type 'y' or 'n' - ") != 'y':
        play = False
        exit()

    clear = lambda: os.system('cls')
    
    clear()
    print(logo)

    for i in range(2):
        player_card.append(deal_card(player_card))
        computer_card.append(deal_card(computer_card))

    player_score = sum_score(player_card)
    computer_score = sum_score(computer_card)

    print(f"    Your cards : {player_card}, current score : {player_score}")
    print(f"    Computer's first card : {computer_card[0]}")

    if has_blackjack(player_card):
        if has_blackjack(computer_card):
            print("You loose ! Computer has blackjack")
            game_continue = False
        else:
            print("You win ! You have blackjack")
            game_continue = False

    if player_score > 21:
        can_hand = False

    if game_continue:
        while can_hand:

            another_card = input("Type 'y' to get another card, type 'n' to pass : ")

            if another_card == 'y':
                player_card.append(deal_card(player_card))
                player_score = sum_score(player_card)

                if player_score > 21:
                    can_hand = False

                print(f"    Your cards : {player_card}, current score : {player_score}")
                print(f"    Computer's first card : {computer_card[0]}")
            else:
                can_hand = False

        while computer_score < 16:
            computer_card.append(deal_card(computer_card))
            computer_score = sum_score(computer_card)

        print(f"    Your final hand : {player_card}, final score : {player_score}")
        print(f"    Computer's final hand : {computer_card} , final score : {computer_score}")

        condition_game(score_player=player_score, score_computer=computer_score)