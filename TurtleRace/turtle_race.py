import random
from turtle import Turtle, Screen

colors = ["red", "green", "yellow", "blue", "orange"]


class Race:
    colors = ["red", "green", "yellow", "blue", "orange"]
    turtle_c = []

    def __init__(self, number):
        self.no_of_turtle = number

    def get_turtle(self, tcolor):
        t = Turtle(shape="turtle")
        t.shape("turtle")
        t.color(tcolor)
        return t

    def give_turtle_life(self):
        turtles_list = []
        for i in range(1, self.no_of_turtle + 1):
            turtles_list.append(self.get_turtle(colors[i - 1]))
        y = -150
        for kach in turtles_list:
            kach.penup()
            kach.color()
            kach.setposition(-380, y + 20)
            y = y + 40
        return turtles_list

    def race_turtles(self, turtles_list):
        game_end = False
        while not game_end:
            for t in turtles_list:
                t.forward(random.randint(0, 50))
                if (t.position()[0]) > 380:
                    True
                    return t


screen = Screen()
screen.setup(width=800, height=500)
user_trurtle = screen.textinput("Lets Play! Turtle Race",
                                'Please enter turtle color "red", "green", "yellow", "blue", "orange" ')
race = Race(number=5)
turtles_list = race.give_turtle_life()
winner = race.race_turtles(turtles_list)
if user_trurtle == winner.color()[0]:
    print(f"Congratulations ! You Win -- > {winner.color()[0]} Turtle is a Winner  ")
else:
    print(f"Ohh ! better luck next time -- > {winner.color()[0]} Turtle is a Winner  ")

screen.exitonclick()
