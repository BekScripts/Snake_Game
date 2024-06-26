from snake import Snake
from turtle import Screen
import time
from food import Food
from score_board import Score_Board


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("pink")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score_Board()

game_is_on = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.move_food()
        snake.extend()
        score.score_count()

    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        score.reset()
        snake.reset()
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()



