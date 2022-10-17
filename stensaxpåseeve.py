import random

computer1_name = input("What do you want to call computer 1? ")
computer2_name = input("What do you want to call computer 2? ")
play = "yes"
computer1_points = 0
computer2_points = 0
while play == "yes":
    computer1 = random.choice(["rock", "paper", "scissors"])
    computer2 = random.choice(["rock", "paper", "scissors"])
    print(f"\n{computer1_name} chose {computer1} and {computer2_name} chose {computer2}.\n")
    if computer1 == "rock" and computer2 == "scissors" or computer1 == "paper" and computer2 == "rock" or computer1 == "scissors" and computer2 == "paper":
        print(f"{computer1_name} wins!")
        computer1_points += 1
    elif computer1 == "scissors" and computer2 == "rock" or computer1 == "rock" and computer2 == "paper" or computer1 == "paper" and computer2 == "scissors":
        print(f"{computer2_name} wins!")
        computer2_points += 1

    else:
        print("Draw!")
    print(f"\n{computer1_name} has {computer1_points} points and {computer2_name} has {computer2_points}\n")
    play = input("Do you want to play again? ")