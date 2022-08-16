from random import randint
from turtle import Turtle, Screen

is_race_on = False
turtles = []

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()
screen.setup(500, 400)
user_choice = screen.textinput(title="Make your bet", prompt="Which turtle will win the race ? Enter a color : ")

for _ in range(6):
    t = Turtle(shape="turtle")
    turtles.append(t)
    t.penup()
    t.color(colors[_])
    t.goto(x=-230, y=-100 + (_ * 40))

if user_choice:
    is_race_on = True

while is_race_on:
    for t in turtles:
        if t.xcor() > 230:
            is_race_on = False
            
            if user_choice ==  t.pencolor():
                print(f"You've won ! The {t.pencolor()} turtle is the winner !")
            else:
                print(f"You've lost ! The {t.pencolor()} turtle is the winner !")
        else:
            t.forward(randint(0, 10))

screen.exitonclick()