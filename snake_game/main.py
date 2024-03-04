from turtle import Screen, Turtle
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game ')
screen.tracer(0)

snake = Snake()
snake.create_snake()
 

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move_snake()
    
    # all_sapp[0].left(90)



    














screen.exitonclick()