from turtle import Screen
from time import sleep
import turtle
from food import Food
from snake import Snake
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake(3)
food = Food()
score = Score()

screen.listen()

screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

game_is_on = True

while game_is_on:
    snake.move()

    if snake.snake_body[0].distance(food) < 15:
        food.random_location()
        score.update_score()
        snake.extend()

    if snake.snake_body[0].xcor() > 275 or snake.snake_body[0].xcor() < -275:
        game_is_on = False
        score.game_over()
    
    if snake.snake_body[0].ycor() > 275 or snake.snake_body[0].ycor() < -275:
        game_is_on = False
        score.game_over()

    for segment in snake.snake_body[1:]:
        if snake.snake_body[0].distance(segment) < 10:
            game_is_on = False
            score.game_over()

    sleep(0.1)
    screen.update()

screen.exitonclick()