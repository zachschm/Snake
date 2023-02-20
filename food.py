from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    # creates another food pill after being eaten
    def refresh(self):
        x = randint(-250, 250)
        y = randint(-250, 250)
        self.goto(x, y)
