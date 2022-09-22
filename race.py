import turtle, random
hope = input("who will win? ").lower()
bet = int(input("whats your bet? "))
adam = turtle.Turtle()
bart = turtle.Turtle()
adam.penup
bart.penup
adam.goto(-200,50)
bart.goto(-200,-50)
win = False
while win == False:
    adam.forward(random.randint(10,100))
    bart.forward(random.randint(10,100))
    if abs (adam.xcor()) > 250:
        win = True
        winner = "adam"
        print("Adam wins")
    elif abs(bart.xcor()) > 250:
        win = True
        winner = "bart"
        print("Bart wins")
print(f"you betted on {hope}")
if hope == winner:
    print(f"You won you now have {bet*2} credits")
else:
    print("you lost")
turtle.done()