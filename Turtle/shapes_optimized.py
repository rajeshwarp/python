from turtle import Turtle, Screen


class DrawShapes:

    def __init__(self):
        self.my_turtle = Turtle()

    def draw_shapes(self, shape_sides, moves):
        angle = 360 / shape_sides
        for _ in range(0, shape_sides):
            self.my_turtle.forward(moves)
            self.my_turtle.right(angle)


color = ["DarkOrange", "purple", "brown", "red", "yellow", "green", "dark magenta", "alice blue", "purple", "brown"]
draw = DrawShapes()
for i in range(3, 11):
    draw.draw_shapes(i, 25)
    draw.my_turtle.color(color[i - 3])

screen = Screen()
screen.exitonclick()
