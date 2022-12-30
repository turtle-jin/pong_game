from turtle import Turtle


class Paddle(Turtle):
    """A simple attempt to model a paddle"""
    def __init__(self, position, color):
        """initialize the paddle attributes"""
        super().__init__()

        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)