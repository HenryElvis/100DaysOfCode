from tkinter import CENTER
from turtle import Turtle

FONT = ("Arial", 14, "normal")
FONT_GAME_OVER = ("Arial", 18, "bold")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.goto(x=0, y=270)
        self.display_score()

    def clear_score(self):
        self.clear()

    def update_score(self):
        self.clear_score()
        self.score += 1
        self.display_score()

    def display_score(self):
        self.write(arg=f"Score : {self.score} High Score: {self.high_score}", align="center", move=False, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over.", align="center", move=False, font=FONT_GAME_OVER)

    def reset_score(self):
        self.clear()
        if self.score > self.high_score:
            with open("data.txt", mode="w") as file:
                self.high_score = self.score
                file.write(str(self.high_score))
        
        self.score = 0
        self.display_score()