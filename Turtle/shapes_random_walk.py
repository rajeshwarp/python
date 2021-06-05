import turtle
from turtle import Turtle, Screen
import random


class DrawShapes:

    def __init__(self):
        self.my_turtle = Turtle()
        turtle.colormode(255)

    def random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = (r, g, b)
        return color

    def draw_shapes(self, moves):
        self.my_turtle.pensize(10)
        self.my_turtle.color(self.random_color())
        directions = [0, 90, 180, 270]
        self.my_turtle.setheading(random.choice(directions))
        self.my_turtle.speed("fastest")
        self.my_turtle.forward(moves)


draw = DrawShapes()

for i in range(1, 200):
    draw.draw_shapes(30)
    # draw.my_turtle.color(random.choice(color))

screen = Screen()
screen.exitonclick()
