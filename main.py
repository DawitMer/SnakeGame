from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.bgcolor("black")
screen.setup(height = 400, width = 500)
screen.title("Snake Game")
screen.tracer(0)

game_is_on = True
snake = Snake()

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

screen.exitonclick()