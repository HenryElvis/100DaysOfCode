import turtle
import pandas

data = pandas.read_csv("50_states.csv")

data_states = data.state

screen = turtle.Screen()
t = turtle.Turtle()
t.penup()
t.hideturtle()

screen.setup(width=800, height=600)

screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

game_is_on = True
score = 0
title = "Guess the State"

states_guessed = []

while game_is_on:
    if score > 0:
        title = f"{score}/50 States Correct"

    answer = screen.textinput(title=title, prompt="What's another state's name ?").capitalize()

    if answer == "Q":
        game_is_on = False
        break

    if answer not in states_guessed:
        for state in data_states:
            if state == answer:
                current_state = data[data.state == state]
                t.goto(int(current_state.x), int(current_state.y))
                t.write(state)
                score += 1
                states_guessed.append(answer)
        print(states_guessed)

# screen.exitonclick()