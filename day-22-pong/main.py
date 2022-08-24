from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    ball.move()
    scoreboard.update_scoreboard()
    if ball.distance(right_paddle)<44.72 and ball.xcor()>330 or ball.distance(left_paddle)<44.72 and ball.xcor()<-330:
        if ball.heading() == 45 or ball.heading() == 225:
            new_heading = ball.heading() + 90
            ball.setheading(new_heading)
        elif ball.heading() == 315 or ball.heading() == 135:
            new_heading = ball.heading() - 90
            ball.setheading(new_heading)
    if ball.xcor() > 390 :
        scoreboard.left_score += 1
        ball.reset_position()
    if ball.xcor() < -390:
        scoreboard.right_score += 1
        ball.reset_position()





screen.exitonclick()
