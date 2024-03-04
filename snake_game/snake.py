from turtle import Turtle
SARTING_POSITIN = [(0, 0), (-20, 0), (-40, 0)]
class Snake:

    def __init__(self):
        self.all_sapp = []


    def create_snake(self):

        for i in SARTING_POSITIN:
            sapp = Turtle('square')
            sapp.penup()
            sapp.color('white')
            sapp.goto(i)
            self.all_sapp.append(sapp)

    def move_snake(self):
        for seg in range(len(self.all_sapp) - 1, 0, -1):
            new_x = self.all_sapp[seg - 1].xcor()
            new_y = self.all_sapp[seg - 1].ycor()
            self.all_sapp[seg].goto(new_x, new_y)
        self.all_sapp[0].forward(20)
    

