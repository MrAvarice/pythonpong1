from turtle import Screen
from ball import Ball
from paddle import Paddle
from line import Line
from score import Score
import time

score = Score()

paddle = Paddle()
line = Line()
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.listen()
screen.onkey(paddle.go_up2, "Up")
screen.onkey(paddle.go_down2, "Down")

screen.onkey(paddle.go_up, "w")
screen.onkey(paddle.go_down, "s")
ball = Ball()
game_is_on = True
ball_moves = ball.move()
x = 0.1
while game_is_on:
    time.sleep(x)
    screen.update()
    ball.move()
    # bounce ball off top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # ball hits paddles
    if ball.distance(paddle.rod) < 55 and ball.xcor() > 320 or ball.distance(paddle.tod) < 55 and ball.xcor() < -320:
        ball.bounce_x()
        ball.faster()
        x = 0

    # ball goes out of bounds
    if ball.xcor() > 380:
        ball.reset_position()
        score.lscore()
        x = 0.1

    if ball.xcor() < -380:
        ball.reset_position()
        score.rscore()
        x =0.1




screen.exitonclick()
