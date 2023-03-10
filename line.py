from turtle import Turtle


class Line:
    def __init__(self):
        self.line()

    def line(self):
        tim = Turtle(shape="arrow")
        tim.hideturtle()
        tim.color("white")
        tim.left(90)
        tim.penup()
        tim.goto(0, -290)
        tim.pensize(7)
        for line in range(30):
            tim.speed(100)
            tim.pendown()
            tim.forward(10)
            tim.penup()
            tim.forward(10)
