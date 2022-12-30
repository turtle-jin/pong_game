from turtle import Turtle
import random


class Ball(Turtle):
    """A simple attempt to model a ball"""
    def __init__(self):
        super().__init__()
        self.color("orange")
        self.shape("circle")
        self.penup()
        self.x_move_step = 10
        self.y_move_step = 5

    def first_serve(self):
        direction = [1, -1]
        choose_direction_x = random.choice(direction)
        choose_direction_y = random.choice(direction)
        self.x_move_step *= choose_direction_x
        self.y_move_step *= choose_direction_y

        self.move()

    def move(self):
        """make the ball move to a random quadrant"""
        x = self.xcor()+self.x_move_step
        y = self.ycor()+self.y_move_step
        self.goto(x, y)

    def bounce_to_wall(self):
        """make the ball bounce and change direction when it hits top and bottom wall"""
        self.y_move_step = -1 * self.y_move_step

    def bounce_to_paddle(self):
        """make the ball bounce and change direction when it hits the paddle"""
        self.x_move_step = -1 * self.x_move_step

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_to_paddle()








