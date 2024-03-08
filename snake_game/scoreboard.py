from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')


class Score(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.high_score = self.prev_high()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.prev_high()
        self.update_score()

    def prev_high(self):
        with open('highscore.txt', mode='r') as score_file: 
            self.high_score = int(score_file.read())
        return self.high_score

    def update_score(self):
        self.clear()
        self.write(f'Score = {self.score} High Score = {self.high_score}', move= False, align= ALIGNMENT,  font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_score()
    
    def reset(self):
        self.high_score = max(self.high_score, self.score)
        self.score = 0
        self.update_score()

        with open('highscore.txt', mode='w') as score_file: 
            score_file.write(f"{self.high_score}")
        
    # def game_over(self):
    #     self.color('white')
    #     self.hideturtle()
    #     self.penup()
    #     self.goto(0,0)
    #     self.write('Game Over...', move= False, align= ALIGNMENT,  font=FONT)
    #     self.high_score = max(self.score, self.high_score)

    

