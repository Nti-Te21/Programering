import turtle, random

adam = turtle.Turtle()
adam.speed(0)
while True:
    adam.color(random.random(), random.random(), random.random())
    adam.circle(100 , 140)
    adam.right(random.randint(10,30))
    adam.forward(290)
    if abs (adam.xcor()) > 400 or abs (adam.ycor()) > 400:
        adam.penup
        adam.goto(0,0)
        adam.pendown
turtle.done()