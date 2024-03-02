import turtle as t
billa = t.Turtle()
import random


billa.shape("turtle")

# for _ in range(4):
#     billa.forward(100)
#     billa.right(90)

# for _ in range(15):
#     billa.forward(10)
#     billa.penup()
#     billa.forward(10)
#     billa.pendown()


# Challenge 3
# def shape(num_sides):
#     angle = 360 // num_sides
#     billa.color(random.choice(colors))
#     for k in range(num_sides):
#         billa.forward(100)
#         billa.left(angle)
        

# for j in range(3, 11):
#     shape(j)



# Challenge 4
colors = ['Tomato', 'IndianRed', 'Tan', 'SlateGrey', 'Wheat', 'DeepPink', 'Purple', 'NavajoWhite', 'RosyBrown']
directions = [90, 180, 270, 360]
billa.speed('fastest')
billa.width(10)
t.colormode(255)
def random_color():
    r = random.randint(1, 256)
    g = random.randrange(1, 256)
    b = random.randrange(1, 256)
    return (r, g, b)

for _ in range(200):
    billa.forward(30)
    billa.setheading(random.choice(directions))
    billa.pencolor(random_color())
    



















screen = t.Screen()
screen.exitonclick()