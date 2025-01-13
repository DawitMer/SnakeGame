from turtle import Screen
import time

from scoreboard import ScoreBoard
from snake import Snake
from food import Food

screen = Screen()
screen.bgcolor("black")
screen.setup(height = 600, width = 600)
screen.title("Snake Game")
screen.tracer(0)

game_is_on = True
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


while game_is_on:
    screen.update()
    time.sleep(0.1)
    # for square in segment:
    #     square.forward(20)
    # segment[0].left(90)
    snake.move()

    if snake.head.distance(food) < 20:
        scoreboard.increase_score()
        food.refresh()
        snake.extend()

    if snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290:
        scoreboard.game_over()
        game_is_on = False

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()