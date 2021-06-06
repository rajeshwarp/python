from turtle import Turtle, Screen


class Directions:
    def __init__(self):
        self.tim = Turtle()

    def move_forward(self):
        self.tim.forward(10)

    def move_back(self):
        self.tim.backward(10)

    def move_clockwise(self):
        self.tim.left(10)

    def move_anti_clockwise(self):
        self.tim.right(10)

    def move_clear(self):
        self.tim.reset()


screen = Screen()
screen.listen()
stylus = Directions()
screen.onkeypress(key="f", fun=stylus.move_forward)
screen.onkeypress(key="s", fun=stylus.move_back)
screen.onkeypress(key="a", fun=stylus.move_anti_clockwise)
screen.onkeypress(key="d", fun=stylus.move_clockwise)
screen.onkeypress(key="c", fun=stylus.move_clear)
screen.exitonclick()
