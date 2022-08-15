from turtle import Screen
import turtle as turtle
from random import randint, choice

t = turtle.Turtle()

turtle.colormode(255)

t.shape("turtle")
t.color("red")

# for i in range(4):
#     t.forward(100)
#     t.right(90)

# for _ in range(15):
#     t.forward(10)
#     t.penup()
#     t.forward(10)
#     t.pendown()


number_side = 3
# t.hideturtle()
color_list = ["cornflower blue", "spring green", "orange", "pale green", "peach puff", "violet", "orchid", "orange red", "light coral", "saddle brown", ]

def random_color():
    color = choice(color_list)
    # color_list.remove(color)

    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    rgb_color = (r, g, b)

    return rgb_color

# for _ in range(5):
#     t.color(random_color())
#     for i in range(number_side):
#         t.forward(100)
#         t.right(360 / number_side)
#     number_side += 1

# direction_list = [0, 90, 180, 270]

# t.width(15)

# for _ in range(200):
#     t.color(random_color())
#     t.setheading(choice(direction_list))
#     t.forward(25)
#     t.speed("fast")

t.speed("fastest")

for _ in range(0, 360, 5):
    t.color(random_color())
    t.circle(100)
    t.setheading(_)

screen = Screen()
screen.exitonclick()