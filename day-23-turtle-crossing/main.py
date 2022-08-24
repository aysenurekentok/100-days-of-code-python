import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create()
    car_manager.move()

    # Detect
    for car in car_manager.all:
        if car.distance(player) < 25:
            game_is_on = False

    # Cross
    if player.crossed_the_road():
        player.start_again()
        car_manager.level_up()

screen.exitonclick()