from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.penup()
        self.color('white')
        self.refresh_location()
    
    def refresh_location(self):
        self.random_x = randint(a=-280,b= 280)
        self.random_y = randint(a=-280, b=280)
        self.goto(x=self.random_x, y=self.random_y)
