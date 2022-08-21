from random import randint, choice
from turtle import Turtle
import turtle

color_palette = ["red", "light sky blue", "medium spring green", "medium violet red"]

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.random_location()

    def random_color(self):
        self.color(choice(color_palette))

    def random_location(self):
        self.random_color()
        x, y = randint(-280, 280), randint(-280, 280)
        self.goto(x, y)