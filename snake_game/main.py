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
snake.speed('fast')
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

    # Collision with food 
    if snake.head.distance(food) < 15:
        food.refresh_location()
        snake.extend()
        score_board.increase_score()
        

    # Collision with wall
    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        snake.reset()
        score_board.reset()
        # score_board.game_over()

    
    # Detect Collision with tail
    for sapp in snake.all_sapp[1:]:
        if snake.head.distance(sapp) < 10:
            snake.reset()
            score_board.reset()
            
            # score_board.game_over()
            

        




screen.exitonclick()