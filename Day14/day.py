from random import randint
import logo
import data
import os

clear = lambda : os.system("cls")

dictionnary = {
    "Rihanna": 411,
    "Ronaldo": 474,
    "Shakira": 76,
    "Neymar": 177,
    "Macron": 3,
    "Elon Musk": 102,
    "Selena Gomez": 342
}

def get_result(index_a, index_b):
    if data.data[index_a]["follower_count"] > data.data[index_b]["follower_count"]:
        return 'a'
    else:
        return 'b'

def player_score(answer, player_answer, score):
    if answer == player_answer:
        return 1
    else:
        return 0

def game_manager(answer, player_answer, score):
    if player_score(answer, player_answer, score) == 1:
        print(f"You're right! current score : {score +1}")
        return True
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        return False

restart = True

while restart:
    score = 0
    player_won = True

    clear()

    while player_won:
        clear()
        print(logo.logo_title)

        index_first_person = randint(0, len(data.data) -1)
        index_second_person = randint(0, len(data.data) -1)
        
        first_person = data.data[index_first_person]["name"]
        second_person = data.data[index_second_person]["name"]
        result = get_result(index_first_person, index_second_person)

        if score > 0:
            print(f"You're right! current score : {score}")

        print(f"Compare A : {first_person}")
        print(logo.logo_vs)
        print(f"Against B : {second_person}")

        player_result = input("Who has more followers ? Type 'a' or 'b' - ")
        score += player_score(result, player_result, score=score)

        player_won = game_manager(result, player_result, score=score)

        if player_won == False:
            if input("Restart a game ? 'y' or 'n'") == 'y':
                restart = True
            else:
                restart = False