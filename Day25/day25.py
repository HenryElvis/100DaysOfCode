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

while game_is_on:
    if score > 0:
        title = f"{score}/50 States Correct"

    answer = screen.textinput(title=title, prompt="What's another state's name ?")

    if answer == "q":
        game_is_on = False

    for state in data_states:
        if state == answer.capitalize():
            current_state = data[data.state == state]
            t.goto(int(current_state.x), int(current_state.y))
            t.write(state)
            score += 1

# screen.exitonclick()