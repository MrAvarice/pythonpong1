from turtle import Turtle, Screen
import random

X = 3

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("teal")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speed(X)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def faster(self):
        global X
        X += 5

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def reset_position(self):
        self.hideturtle()
        self.goto(0, 0)
        self.showturtle()
        self.bounce_x()