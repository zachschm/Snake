from turtle import Turtle
# Constants
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # Creates the base snake
    def create_snake(self):
        x: int = 0
        for i in range(4):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(x, 0)
            x -= 20
            self.segments.append(new_segment)

    # Moves all parts of the snake
    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)
        self.segments[0].forward(20)

    # Changes snake heading to 90
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # Changes snake heading to 270
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # Changes snake heading to 180
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # Changes snake heading to 0
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # Adds additional segment to lengthen the snake upon the eating of a food pill
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # Helper function for add_segment()
    def extend(self):
        # negative numbers in python lists can count from the back
        # this -1 gets a hold of the last segment's position
        self.add_segment(self.segments[-1].position())

