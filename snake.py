from turtle import Turtle

# in python constants are named with all CAPS
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0), (-60, 0), (-80, 0)]
MOVE_DISTANCE = 15
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POSITION:
            self.add_snake(pos)

    def add_snake(self, position):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("yellow")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def increase_snake_size(self):
        # extend tale of snake
        self.add_snake(self.segments[-1].position())

    def move(self):
        # for seg_num in range(start = len(segments)-1 , stop=0, step = -1)
        for seg_num in range(len(self.segments) - 1, 0, -1):
            STARTING_POSITION = self.segments[seg_num - 1].pos()
            self.segments[seg_num].goto(STARTING_POSITION)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)