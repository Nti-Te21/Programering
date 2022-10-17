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
    