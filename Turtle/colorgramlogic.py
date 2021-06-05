import random
import turtle
import colorgram
from turtle import Turtle, Screen

turtle.colormode(255)
tim = Turtle()
tim.penup()
screen = Screen()
colors = tuple(colorgram.extract('dam.jpg', 20))
y = 0
for _ in range(1, 10):
    for _ in range(1, 10):
        color = random.choice(colors)
        tim.pencolor(color.rgb.r, color.rgb.g, color.rgb.b)
        tim.dot(20)
        tim.forward(30)
    tim.setx(0)
    y = y + 30
    tim.sety(y)


screen.exitonclick()
