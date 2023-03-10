from turtle import Turtle, Screen
import turtle

screen = Screen()
LEFT_P = [(-390, 20), (-390, 0), (-390, -20)]

RIGHT_P = [(380, 20), (380, 0), (380, -20)]

MOVE = 20


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.todd()
        self.go_up()
        self.go_down()
        self.rodd()
        # self.go_up2()
        # self.go_down2()

    def todd(self):
        self.tod = Turtle(shape="square")
        self.tod.color("white")
        self.tod.penup()
        self.tod.shapesize(stretch_wid=5, stretch_len=1)
        self.tod.goto(-350, 0)

    def rodd(self):
        self.rod = Turtle(shape="square")
        self.rod.color("white")
        self.rod.penup()
        self.rod.shapesize(stretch_wid=5, stretch_len=1)
        self.rod.goto(350, 0)

    def go_up(self):
        new_y = self.tod.ycor() + 40
        self.tod.goto(self.tod.xcor(), new_y)

    def go_down(self):
        new_y = self.tod.ycor() - 40
        self.tod.goto(self.tod.xcor(), new_y)

    def go_up2(self):
        new_x = self.rod.ycor() + 40
        self.rod.goto(self.rod.xcor(), new_x)

    def go_down2(self):
        new_t = self.rod.ycor() - 40
        self.rod.goto(self.rod.xcor(), new_t)
