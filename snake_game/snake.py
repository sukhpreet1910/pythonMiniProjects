from turtle import Turtle
SARTING_POSITIN = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.all_sapp = []
        self.create_snake()
        self.head = self.all_sapp[0]


    def create_snake(self):

        for i in SARTING_POSITIN:
            self.add_segament(i)
            

    def add_segament(self, position):
        sapp = Turtle('square')
        sapp.penup()
        sapp.color('white')
        sapp.goto(position)
        self.all_sapp.append(sapp)

    def extend(self):
        self.add_segament(self.all_sapp[-1].position())


    def move_snake(self):
        for seg in range(len(self.all_sapp) - 1, 0, -1):
            new_x = self.all_sapp[seg - 1].xcor()
            new_y = self.all_sapp[seg - 1].ycor()
            self.all_sapp[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            # self.move_snake()
            self.head.seth(90)

    def down(self):
        if self.head.heading() != UP:
            # self.move_snake()
            self.head.seth(270)

    def right(self):
        # self.move_snake()
        if self.head.heading() != LEFT:
            self.head.seth(0)
    
    def left(self):
        # self.move_snake()
        if self.head.heading() != RIGHT:
            self.head.seth(180)

    

