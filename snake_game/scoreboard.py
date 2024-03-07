from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')




class Score(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.write(f'Score = {self.score}', move= False, align= ALIGNMENT,  font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
        
    def game_over(self):
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0,0)
        self.write('Game Over...', move= False, align= ALIGNMENT,  font=FONT)



        
        
