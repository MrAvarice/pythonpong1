from turtle import Turtle, Screen
screen = Screen()
l_count = 0
r_count = 0
class Score(Turtle):

    def __init__(self):
        super().__init__()
        # self.color("white")
        # self.penup()
        self.l_count = 0
        self.r_count = 0
        self.l_score()
        self.r_score()
        self.update()
        self.update2()



    def l_score(self):
        self.rim = Turtle(shape= "arrow")
        self.rim.hideturtle()
        self.rim.penup()
        self.rim.goto(-25, 280)
        self.rim.color("white")
        self.rim.write(f"{self.l_count}", False, align="left", font=("Arial",14))
        

    def r_score(self):
        self.tim = Turtle(shape= "arrow")
        self.tim.hideturtle()
        self.tim.penup()
        self.tim.goto(20, 280)
        self.tim.color("white")
        self.tim.write(f"{self.r_count}", False, align="left", font=("Arial",14))

    def update(self):
        self.rim.write(f"{self.l_count}", False, align="left", font=("Arial", 14))

    def update2(self):
        self.tim.write(f"{self.r_count}", False, align="left", font=("Arial", 14))

    def rscore(self):
        self.r_count += 1
        self.tim.clear()
        self.update2()


    def lscore(self):
        self.l_count += 1
        self.rim.clear()
        self.update()