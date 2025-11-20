import turtle

import colorgram
from turtle import Turtle, Screen
import random

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

color_list = [(246, 242, 235), (248, 242, 245), (240, 246, 242),
              (239, 242, 247), (198, 165, 116), (144, 79, 55),
              (221, 201, 138), (58, 93, 121), (167, 153, 48),
              (132, 34, 23), (137, 162, 181), (69, 40, 34),
              (51, 117, 87), (195, 93, 75), (146, 178, 150),
              (18, 93, 72), (231, 176, 165), (162, 143, 158),
              (35, 60, 75), (105, 73, 77), (180, 204, 177),
              (148, 19, 23), (83, 147, 127), (70, 37, 40),
              (18, 70, 60), (27, 82, 88), (40, 66, 89),
              (190, 86, 89), (68, 64, 58), (223, 176, 180)]

tim = Turtle()
tim.speed("fastest")
turtle.colormode(255)

tim.penup()
tim.hideturtle()
tim.goto(-200, -200)

for dot_count in range(1, 101):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




my_screen = Screen()
my_screen.exitonclick()