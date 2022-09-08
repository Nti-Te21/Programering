import random

computer = random.choice(["rock", "paper", "scissors"])

user = input("rock, paper or scissors? ")

print("The computer chose", computer,"and the user chose", user +".")

# TODO - Implement the if statements that prints who wins

if computer == "rock" and user == "scissors" or computer == "paper" and user == "rock" or computer == "scissors" and user == "paper":
    print("Computer wins!")
elif computer == "scissors" and user == "rock" or computer == "rock" and user == "paper" or computer == "paper" and user == "scissors":
    print("User wins!")
else:
    print("Draw!")