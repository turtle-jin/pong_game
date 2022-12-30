from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from score import Scoreboard
from tkinter import *
from tkinter import messagebox
root = Tk()

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My PingPong Game")
screen.tracer(0)  # if use tracer, you will need to update the screen

# line in the middle
turtle = Turtle()
turtle.pencolor("white")
turtle.ht()
turtle.pensize(10)
turtle.penup()
turtle.setheading(270)
turtle.backward(300)

for i in range(15):
    turtle.pendown()
    turtle.forward(20)
    turtle.penup()
    turtle.forward(20)

right_paddle = Paddle((350, 0), "teal")
left_paddle = Paddle((-350, 0), "purple")
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.02)
    screen.update()

    if ball.xcor() == 0 and ball.ycor() == 0 and scoreboard.l_score == 0 and scoreboard.r_score == 0:
        ball.first_serve()

    ball.move()


    # Detect collision with upper and bottom wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_to_wall()

    # Detect collision with the paddle
    if ball.distance(right_paddle) <= 50 and ball.xcor() >= 320:
        ball.bounce_to_paddle()

    if ball.distance(left_paddle) <= 50 and ball.xcor() <= -320:
        ball.bounce_to_paddle()

    # Detect when Right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_earn_point()

    # Detect when Left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_earn_point()

    if scoreboard.l_score == 11:
        game_is_on = False
        messagebox.showinfo("Winner", "Purple is the winner!")
        root.mainloop()

    if scoreboard.r_score == 11:
        game_is_on = False
        messagebox.showinfo("Winner", "Blue is the winner!")
        root.mainloop()



screen.exitonclick()
