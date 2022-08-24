from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.setheading(45)

    def move(self):
        self.forward(10)
        if self.ycor() > 285 or self.ycor() < -285:
            new_heading = 360 - self.heading()
            self.setheading(new_heading)

    def reset_position(self):
        self.goto(0,0)





