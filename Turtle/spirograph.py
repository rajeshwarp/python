import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
i = 0
tim.speed("fastest")

turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


for i in range(0, 360, 5):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(i)

screen = Screen()
screen.exitonclick()
