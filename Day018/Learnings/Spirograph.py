import turtle
from turtle import Turtle, Screen
import random


tim = Turtle()
tim.speed("fastest")
turtle.colormode(255)
tim.hideturtle()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


for _ in range(0, 361, 5):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(_)

my_screen = Screen()
my_screen.exitonclick()