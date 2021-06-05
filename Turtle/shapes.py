from turtle import Turtle, Screen


class DrawShapes:

    def __init__(self):
        self.my_turtle = Turtle()

    def triangle(self):
        for _ in range(1, 4):
            self.my_turtle.forward(50)
            self.my_turtle.right(120)

    def square(self):
        self.my_turtle.forward(50)
        for _ in range(1, 4):
            self.my_turtle.right(90)
            self.my_turtle.forward(50)
        self.my_turtle.right(90)

    def pentagon(self):
        for _ in range(1, 6):
            self.my_turtle.forward(50)
            self.my_turtle.right(72)

    def hexagon(self):
        for _ in range(1, 7):
            self.my_turtle.forward(50)
            self.my_turtle.right(60)

    def heptagon(self):
        for _ in range(1, 8):
            self.my_turtle.forward(50)
            self.my_turtle.right(51.42)

    def octagon(self):
        for _ in range(1, 9):
            self.my_turtle.forward(50)
            self.my_turtle.right(45)

    def change_color(self, change_color):
        self.my_turtle.pencolor(change_color)


draw = DrawShapes()
draw.triangle()
draw.change_color("red")
draw.square()
draw.change_color("yellow")
draw.pentagon()
draw.change_color("brown")
draw.hexagon()
draw.change_color("blue")
draw.heptagon()
draw.change_color("green")
draw.octagon()

screen = Screen()
screen.exitonclick()
