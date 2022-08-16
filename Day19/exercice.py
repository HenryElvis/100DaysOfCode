from cgitb import reset
from turtle import Turtle, Screen

t = Turtle()


def movement(func):
    func()

def move_forward():
    t.forward(20)

def move_backward():
    t.forward(20)

def turn_right():
    heading = t.heading() + 10
    t.setheading(heading)

def turn_left():
    heading = t.heading() - 10
    t.setheading(heading)

def clear_screen():
    t.reset()
    # t.clear()

screen = Screen()
screen.listen()

screen.onkey(fun=clear_screen, key="c")

screen.onkey(fun=move_forward, key="z")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=turn_left, key="q")
screen.onkey(fun=turn_right, key="d")

screen.exitonclick()