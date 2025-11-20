import turtle
from turtle import Turtle, Screen
import random

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("violet")
my_turtle.penup()
my_turtle.goto(-300, 300)
my_turtle.pendown()
my_turtle.write("Code from 3 to 16", font=("Arial", 12, "bold"))
my_turtle.penup()
my_turtle.goto(-300, 250)
my_turtle.pendown()

for i in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.penup()
timmy.goto(100, 300)
timmy.pendown()
timmy.write("Code from 18 to 33", font=("Arial", 12, "bold"))
timmy.penup()
timmy.goto(100, 250)
timmy.pendown()

for i in range(10):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

turtle_colors = [
    "red", "blue", "green", "yellow", "cyan",
    "magenta", "orange", "purple", "pink", "brown",
    "gray", "black", "gold",
    "navy", "olive", "maroon", "teal", "coral"
]

tim = Turtle()
tim.shape("turtle")
tim.color("red")
tim.penup()
tim.goto(-300, 0)
tim.pendown()
tim.write("Code from 36 to 58", font=("Arial", 12, "bold"))
tim.penup()
tim.goto(-300, -50)
tim.pendown()
for _ in range(3, 9):
    angle = int(360 / _)
    tim.color(random.choice(turtle_colors))
    for i in range(_):
        tim.forward(100)
        tim.right(angle)


timmy2 = Turtle()
directions = [0, 90, 180, 270]
timmy2.pensize(10)
timmy2.penup()
timmy2.goto(150, 0)
timmy2.pendown()
timmy2.write("Code from 61 to 75", font=("Arial", 12, "bold"))
timmy.penup()
timmy2.goto(150, -100)
timmy2.pendown()
timmy2.speed("fastest")
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


for _ in range(200):
    timmy2.color(random_color())
    timmy2.setheading(random.choice(directions))
    timmy2.forward(30)

my_screen = Screen()
my_screen.exitonclick()