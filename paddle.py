from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.speed(0)
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(x=position[0], y=position[1])

    def up(self):
        self.setheading(90)
        self.movement()

    def down(self):
        self.setheading(270)
        self.movement()

    def movement(self):
        self.forward(20)
