from turtle import Turtle
from random import randint
import turtle

class Snake:

    def __init__(self, segment_at_start):
        turtle.colormode(255)
        self.snake_body = []
        self.segment_at_start = segment_at_start
        self.create_snake()

    def create_snake(self):
        for i in range(self.segment_at_start):
            snake = Turtle(shape="square")
            snake.penup()
            snake.color("white")
            snake.setx(-20 * i)
            self.snake_body.append(snake)
        
        self.change_randomly_head_color()

    def reset_game(self):
        for seg in self.snake_body:
            seg.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()

    def move(self):
        for segment in range(len(self.snake_body) -1, 0, -1):
            x = self.snake_body[segment -1].xcor()
            y = self.snake_body[segment -1].ycor()
            self.snake_body[segment].goto(x, y)

        self.snake_body[0].forward(20)

    def change_randomly_head_color(self):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)

        rgb = (r, g, b)
        self.snake_body[0].color(rgb)

    def up(self):
        if self.snake_body[0].heading() != 270:
            self.snake_body[0].setheading(90)

    def down(self):
        if self.snake_body[0].heading() != 90:
            self.snake_body[0].setheading(270)

    def right(self):
        if self.snake_body[0].heading() != 180:
            self.snake_body[0].setheading(0)

    def left(self):
        if self.snake_body[0].heading() != 0:
            self.snake_body[0].setheading(180)

    def add_segment(self, position):
        new = Turtle(shape="square")
        new.penup()
        new.color("white")
        new.goto(position)
        self.snake_body.append(new)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())