from random import choice, randint
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2

class CarManager():
    
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def move(self):
        for car in self.cars:
            car.backward(self.speed)

    def hit_player(self, player):
        for car in self.cars:
            if car.distance(player) <= 20:
                return True
            
        return False

    def increase_speed(self):
        self.speed += MOVE_INCREMENT

    def create(self):
        if randint(1, 7) == 1:
            car = Turtle("square")
            car.color(choice(COLORS))
            car.penup()
            car.shapesize(1, 2)
            car.goto(300, randint(-250, 250))
            self.cars.append(car)