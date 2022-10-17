import random
def pve():
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
def pvp():
    user1_name = input("What do you want to call player1? ")
    user2_name = input("What do you want to call player2? ")
    play = "yes"
    user1_points = 0
    user2_points = 0
    while play == "yes":
        user1 = input("rock paper or scissors? ")
        print("""
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """)
        user2 = input("rock, paper or scissors? ")
        print(f"{user1_name} chose {user1} and {user2_name} chose {user2}.")
        if user1 == "rock" and user2 == "scissors" or user1 == "paper" and user2 == "rock" or user1 == "scissors" and user2 == "paper":
            print(f"{user1_name} wins!")
            user1_points += 1
        elif user1 == "scissors" and user2 == "rock" or user1 == "rock" and user2 == "paper" or user1 == "paper" and user2 == "scissors":
            print(f"{user2_name} wins!")
            user2_points += 1

        else:
            print("Draw!")
        print(f"{user1_name} has {user1_points} points and {user2_name} has {user2_points} points")
        play = input("Do you want to play again? ")
def eve():
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
while True:
    menyval = input("\n1. Spela pve\n"
                   "2. Spela pvp\n"
                   "3. Spela eve\n"
                   "4. Avsluta program ")
    if menyval == "1":
        pve()
    if menyval == "2":
        pvp()
    if menyval == "3":
        eve()
    if menyval == "4":
        break