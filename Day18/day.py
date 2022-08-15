import colorgram
import turtle as t
from turtle import Screen
from random import choice

# color = colorgram.extract("image.jpg", 30)
#
# rgb_colors = []
#
# for c in color:
#     r = c.rgb.r
#     g = c.rgb.g
#     b = c.rgb.b
#
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tur = t.colormode(255)

t.hideturtle()
t.penup()
t.backward(200)

for h in range(10):
    for w in range(10):
        t.dot(20, choice(color_list))
        t.forward(50)

    t.setheading(90)
    t.forward(50)
    t.setheading(0)
    t.backward(500)

screen = Screen()
screen.screensize(10, 10)

screen.exitonclick()