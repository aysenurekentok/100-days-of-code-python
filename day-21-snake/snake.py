from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.blocks = []
        self.create_snake()
        self.head = self.blocks[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_block(position)

    def add_block(self, position):
        square = Turtle("square")
        square.color("white")
        square.penup()
        square.goto(position)
        self.blocks.append(square)

    def reset(self):
        for block in self.blocks:
            block.hideturtle()
        self.blocks.clear()
        self.create_snake()
        self.head = self.blocks[0]

    def extend(self):
        self.add_block(self.blocks[-1].position())

    def move(self):
        for i in range(len(self.blocks) - 1, 0, -1):
            new_position = self.blocks[i - 1].position()
            self.blocks[i].goto(new_position)
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



