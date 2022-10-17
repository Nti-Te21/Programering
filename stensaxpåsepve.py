import random

user_name = input("What do you want to call yourself?")
computer_name = input("What do you want to call the computer?")
play = "yes"
cumpeter_points = 0
user_points = 0
while play == "yes":
    computer = random.choice(["rock", "paper", "scissors"])
    user = input("\nrock, paper or scissors?\n")
    print(f"\n{user_name} chose {user} and {computer_name} chose {computer}.")
    if computer == "rock" and user == "scissors" or computer == "paper" and user == "rock" or computer == "scissors" and user == "paper":
        print(f"\n{computer_name} wins!")
        cumpeter_points += 1
    elif computer == "scissors" and user == "rock" or computer == "rock" and user == "paper" or computer == "paper" and user == "scissors":
        print(f"\n{user_name} wins!")
        user_points += 1

    else:
        print("Draw!")
    print(f"\n{user_name} has {user_points} points and {computer_name} has {cumpeter_points}\n")
    play = input("\nDo you want to play again? ")
 