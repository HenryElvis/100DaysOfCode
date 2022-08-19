from turtle import Turtle

class Score(Turtle):

    def __init__(self, pos_score):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.pos_score = pos_score
        self.l_score = 0
        self.r_score = 0
        self.display_score()

    def add_point(self, player_index):
        self.clear()

        if player_index == 0:
            self.l_score += 1
        elif player_index == 1:
            self.r_score +=1

        self.display_score()

    def display_score(self):
        self.goto(self.pos_score, 200)
        self.write(f"{self.l_score}", align="center", font=("Courier", 80, "normal"))
        self.goto(self.pos_score * -1, 200)
        self.write(f"{self.r_score}", align="center", font=("Courier", 80, "normal"))