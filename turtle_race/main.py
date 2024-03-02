import turtle as t
import random
screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Which color will win the race? Enter a color: ")



all_turtles = []
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_axis = [-70, -40, -10, 20, 50, 80]
for index in range(0, 6):
    billa = t.Turtle(shape='turtle')
    billa.penup()
    billa.color(colors[index])
    billa.goto(x=-230, y = y_axis[index])
    all_turtles.append(billa)

game_on = False
if user_bet:
    game_on = True

while game_on:
    for turtle in all_turtles:

        if turtle.xcor() > 230:
            winnig_color = turtle.pencolor()
            if winnig_color == user_bet:
                print(f"You 've won. The {winnig_color.upper()} turle is winner")
            else:
                print(f"Sorry! You 've lost. The {winnig_color.upper()} turle is winner")

            game_on = False

        random_dist = random.randint(0, 10)
        turtle.forward(random_dist)

screen.exitonclick()