from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self, x_cor):
        super().__init__()
        self.x_cor = x_cor
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setx(350 * self.x_cor)

    def up(self):
        self.sety(self.ycor() + 20)

    def down(self):
        self.sety(self.ycor() - 20)