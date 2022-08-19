from turtle import Turtle, Screen, up
from paddle import Paddle
from ball import Ball
from score import Score
from time import sleep

screen = Screen()

screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")

screen.tracer(0)

player = Paddle(-1)
player_ = Paddle(1)

ball = Ball()

score = Score(-100)

screen.listen()

screen.onkey(player.up, "z")
screen.onkey(player.down, "s")

screen.onkey(player_.up, "Up")
screen.onkey(player_.down, "Down")

game_is_on = True

while game_is_on:
    sleep(ball.move_speed)

    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(player) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    if ball.distance(player_) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.add_point(0)

    if ball.xcor() < -380:
        ball.reset_position()
        score.add_point(1)

screen.exitonclick()