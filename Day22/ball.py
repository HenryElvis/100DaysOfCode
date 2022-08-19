from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xdir = 10
        self.ydir = 10
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.xdir, self.ycor() + self.ydir)

    def bounce_y(self):
        self.ydir *= -1
    
    def bounce_x(self):
        self.xdir *= -1
        self.increase_speed()

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.bounce_y()
        self.move_speed = 0.1

    def increase_speed(self):
        self.move_speed *= 0.9