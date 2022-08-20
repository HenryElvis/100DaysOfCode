from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.sety(-280)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def is_run_finish(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        
        return False

    def next_run(self):
        self.goto(STARTING_POSITION)