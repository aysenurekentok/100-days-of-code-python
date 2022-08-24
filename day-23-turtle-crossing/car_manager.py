from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.turtlesize(stretch_wid=1, stretch_len=2)
            car.setheading(180)
            random_y = random.randint(-250, 250)
            car.goto(300, random_y)
            self.all.append(car)

    def move(self):
        for car in self.all:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

