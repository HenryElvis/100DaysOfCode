import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()

car = CarManager()
screen.tracer(0)

screen.listen()

screen.onkey(player.move_up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create()
    car.move()
        
    if car.hit_player(player.pos()):
        score.game_over()
        game_is_on = False

    if player.is_run_finish():
        player.next_run()
        score.increase_score()
        car.increase_speed()

screen.exitonclick()