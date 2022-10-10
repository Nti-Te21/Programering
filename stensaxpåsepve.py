import random

user_name = input("What do you want to call yourself? ")
computer_name = input("What do you want to call the computer? ")
play = "yes"
cumpeter_points = 0
user_points = 0
while play == "yes":
    computer = random.choice(["rock", "paper", "scissors"])
    user = input("rock, paper or scissors? ")
    print(f"The {computer_name} chose {computer} and the {user_name} chose {user}.")
    if computer == "rock" and user == "scissors" or computer == "paper" and user == "rock" or computer == "scissors" and user == "paper":
        print(f"{computer_name} wins!")
        cumpeter_points += 1
    elif computer == "scissors" and user == "rock" or computer == "rock" and user == "paper" or computer == "paper" and user == "scissors":
        print(f"{user_name} wins!")
        user_points += 1

    else:
        print("Draw!")
    print(f"{user_name} has {user_points} points and {computer_name} has {cumpeter_points} ")
    play = input("Do you want to play again? ")
    