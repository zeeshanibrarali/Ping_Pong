from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_score()

    def update_score(self):
        self.goto(x=-100, y=200)
        self.write(arg=self.l_score, align='center', font=('courier', 80, 'normal'))
        self.goto(x=100, y=200)
        self.write(arg=self.r_score, align='center', font=('courier', 80, 'normal'))

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_score()

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_score()
