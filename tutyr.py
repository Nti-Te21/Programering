from random import random
import turtle

adam = turtle.Turtle()
adam.speed(0)
while True:
    adam.circle(100 , 140)
    adam.right( random(1 ,10 ))
    adam.forward(290)
    if abs (adam.xcor()) > 400 or abs (adam.ycor()) > 400:
        adam.penup
        adam.goto(0,0)
        adam.pendow
turtle.done()