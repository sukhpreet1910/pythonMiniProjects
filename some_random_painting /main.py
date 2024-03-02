# import colorgram
import turtle as t
import random as r

# colors = colorgram.extract('image.jpg', 30)
# rgb_list = []
# for c in colors:    
#     r = c.rgb.r
#     g = c.rgb.g
#     b = c.rgb.b
#     rgb_tup = (r, g, b)
#     rgb_list.append(rgb_tup)
# print(rgb_list)

color_list = [(209, 165, 125), (140, 48, 106), (164, 169, 38), (244, 80, 56), (3, 143, 55), (233, 109, 162), (241, 65, 140), (1, 143, 184), (162, 55, 52), (57, 202, 224), (20, 166, 126), (244, 223, 50), (27, 197, 219), (162, 184, 171), (233, 165, 191), (191, 191, 193), (141, 213, 225), (243, 170, 153), (159, 212, 181), (106, 45, 98), (9, 115, 37), (131, 45, 38)]
billa = t.Turtle()
billa.speed('fastest')
t.colormode(255)
billa.penup()
billa.ht()

billa.setheading(225)
billa.forward(200)
billa.setheading(0)
dot_count = 100

for i in range(1, dot_count + 1):
    billa.dot(20, r.choice(color_list))
    billa.fd(30)
    if i % 10 == 0:
        billa.left(90)
        billa.fd(30)
        billa.left(90)
        billa.fd(300)
        billa.seth(0)

screen = t.Screen()
screen.exitonclick()