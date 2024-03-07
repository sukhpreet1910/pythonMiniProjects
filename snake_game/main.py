from turtle import Screen
from food import Food
import time
from snake import Snake
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game ')
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Score()
# snake.create_snake()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')



game_on = True
score = 0
while game_on:
    
    screen.update()
    time.sleep(0.1)
    
    snake.move_snake()
    if snake.head.distance(food) < 15:
        score_board.increase_score()
        food.refresh_location()
    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        game_on = False
        score_board.game_over()




screen.exitonclick()