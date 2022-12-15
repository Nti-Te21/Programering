import random # First import the random module for the ability to use the .shuffle() function

# function to create the deck unshuffeld
def deck_create():
    suits = ["Hearts", "Diamonds","Spades", "Clubs"]
    values = ["King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3" , "2", "Ace"]
    deck = []
# the suits and values lists are added together with a seperating "of" to create the cards 
# properly so they later can be displayed as they would be in a physical deck of cards
    for suit in suits:
        for value in values:
            deck.append(value + " of " + suit)
# the deck variabel is then returned to make it usable in following functions and parts of the program
    return deck

# Define a function to assign the appropriate points values to each card
def def_points (deck):
# A dictionary is created to store the points connected to each card
    points = {}
    for cards in deck:
# Each card is split into each word so the card type can be detected    
        card = cards.split(" ")
# The first word is checked for its value and that is then assigned to the card 
# As by the blackjack rules the cards that have a string value instead of an integer value are given the value of 10 excluding the ace who has an base value of 11
        if card[0] == "King" or card[0] == "Queen" or card[0] == "Jack":
            points[cards] = 10
        elif card[0].isdigit():
            points[cards] = int(card[0])
        elif card[0] == "Ace":
            points[cards] = 11
    return points

# Define a function to create a balance to use for betting later in the program
def deposit():    
    while True:
# The user is asked to input how much they want to deposit
# And if the input is not an integer the user is asked to make it an integer 
# and to make this possible a while loop is used to repeat the question if an unallowed answer is submited
        deposit = input("How much do you want to deposit? ")
        if deposit.isdigit():
            balance = int(deposit)
            print(f"Your balance is now ${balance}")
            return balance
        else:
            print("Deposite must be a number!")
            continue
# The user and dealer recive thier cards
def deal(deck, dealer, user):
    for _ in range(2):
        card_1 = deck.pop(0)
        dealer.append(card_1)
        card_2 = deck.pop(0)
        user.append(card_2)
# As by blackjack rules a card with a value of "Ace" can give both 11 and 1 point, 
# it must be known what the requierments are for these two diffrent states 
# Then this function checks if the point value of the ace card should be 1 or 11
def ace_value_user(user, user_points, ace_user_test):
# First it checks if there is any point to do the comparison
    if user_points > 20 and user_points != "Blackjack!" and user_points != 21 and ace_user_test == 0:
# Then a for loop checks all cards if any of them are an "Ace"
        for index, card in enumerate(user):
            user_card_type = user[index].split()
            if user_card_type[0] == "Ace":
# This makes sure the function dosent keep running lowering the value belove it's intended value      
                ace_user_test += 1
                return True                
# These two else statements make sure the original point value is returned if the function does not give a result to prevent errors encountering None
        else:
            return user_points        
    else:
        return user_points
# Works as the "ace_value_user" function but operates on the dealear variabels instead
def ace_value_dealer(dealer, dealer_points, ace_dealer_test):
    if dealer_points > 20 and dealer_points != "Blackjack!" and dealer_points != 21 and ace_dealer_test == 0:
        for index, card in enumerate(dealer):
            dealer_card_type = dealer[index].split()
            if dealer_card_type[0] == "Ace":
                ace_dealer_test += 1
                return True
        else:
            return dealer_points
    else:
        return dealer_points
# Asks the user how much they want to bet
def function_bet(balance):
    while True:
        bet = (input("How much do you want to bet? "))
        if bet.isdigit():
            bet = int(bet)
            if bet <= balance and bet > 0:
                print(f"Your bet is ${bet}")
                return bet
            else:
                print("Bet must be greater than zero and smaller than your balance")
                continue
        else:
            print("Please enter a valid bet")
            continue

def main():
# Creates and saves the balance to be used for betting    
    balance = deposit()

# Saves the starting balance for later refrence
    initial_balance = balance

# Creates vital variabels for the ability to withdraw your current balance and ending the game
    withdraw_state = True
    withdraw_possibility = 0

# The while loop that runs the program for as long as you have money to bet with and havn't withdrawn your balance and
    while balance > 0 and withdraw_state:

# Ensures that the "ace_value_user" and "ace_value_dealer" functions will run anew every time there is a new round
        ace_user_test = 0
        ace_dealer_test = 0

# Saves the deck as a list  
        deck = deck_create()

# Saves the point value of each card in a dictionary
        card_points = def_points(deck)

# Creates the lists used to store each players card to then be used for displaying card "hands" and points 
        dealer=[]
        user=[]

# Creates variables vital for deciding what happens at the end of the round
        user_state = None
        withdraw_choice = None

# Asks the user if they want to withdraw thier balance but only after one round
        if withdraw_possibility != 0:
            withdraw_choice = input(f"Do you want to withdraw your balance with a value of: ${balance}\n 1. Yes 2. No ").capitalize()

# If the user chooses to witdraw the "witdraw_state" becomes false triggering the end of the program
        if withdraw_choice == "1" or withdraw_choice == "Yes":
            withdraw_state = False
            break
        else:
            pass

# This line makes it so the withdraw input can be shown after first round as the variabel is now not = 0 making it so the if statement can trigger
        withdraw_possibility +=1

# Shuffels the deck so each round is diffrent and fair
        random.shuffle(deck)

# Deals the first four cards to the players
        deal(deck, dealer, user)

# Saves the users bet
        bet = function_bet(balance)

# Saves the dealers points on one card as one of the dealer cards are intially hiden following blackjack rules
        dealer_points = card_points[dealer[0]]

# Saves the users points on deal
        user_points = card_points[user[0]] + card_points[user[1]]

# Checks if the user imidiatelly recived 21 points and then blackjack with an ace card and a card with a point value of 10
# This value is later used for the diffrent payout rules regarding a direct blackjack in Blackjack rules
        if user_points == 21:
            user_points = "Blackjack!"

# Checks if the user has not recived a blackjack but more than 20 points on first deal
# this meaning doubel aces wich if true results in the "ace_value_user" running to ensure the correct amount of points is given
        if user_points != "Blackjack!" and user_points > 20:
            user_points = ace_value_user(user, user_points)

# The while loop covers all of the players actions and thier results after the cards have been dealt         
        while True:
            print(f"\nThe dealer has a {dealer[0]} and a hidden card Points: {dealer_points}. \n\nYou have a {', and a '.join(user)} Points: {user_points} \n")

# Checks if the round for the user is over either as the user has 21 points or "Blackjack!" or if they have busted by reciving more than 21 points         
            while True:            
                if user_points == "Blackjack!" or user_points>= 21:
                    if user_points == 21 or user_points == "Blackjack!":
                        print("Blackjack")
                        user_state = "win"
                    else:
                        print("Bust")
                        user_state = "lose"
                    break
# Asks the user what they want to do and saves its value
                choice = input("1. Hit 2. Stand 3. Double down \n").capitalize()

# Deals the user a new card and adds it's points to the user point total while making sure the point value is correct                
                if choice == "1" or choice == "Hit":
                    hit_card = deck.pop(0)
                    user.append(hit_card)
                    user_points += card_points[user[-1]]
                    if ace_value_user(user, user_points, ace_user_test) == True:
                        user_points -= 10
                        ace_user_test = 1
                    print(f"\nThe dealer has a {dealer[0]} and a hidden card Points: {dealer_points}. \n\nYou have a {', and a '.join(user)} Points: {user_points} \n")

# Gives the turn over to the dealer              
                elif choice == "2" or choice == "Stand":
                    break

# Doubles the bet value and hits once to then immideatly giving the turn over to the dealer
                elif choice == "3" or choice == "Double down":
# Controls one cant bet more than one has in thier balance through doubleing down
                    
                    if bet*2 > balance:
                        print("You can't double down if the double is more than your balance")
                        continue
                    bet = bet*2
                    hit_card = deck.pop(0)
                    user.append(hit_card)
                    user_points += card_points[user[-1]]
# Once again the "ace_valu_user" function is called to ensure all points are recived as intended                  
                    if ace_value_user(user, user_points, ace_user_test) == True:
                        user_points -= 10
                        ace_user_test = 1
# Then a check is performed to se if the user has busted or recived 21 points                     
                    if user_points == "Blackjack!" or user_points >= 21:
                        if user_points == 21 or user_points == "Blackjack!":
                            print("Blackjack")
                            user_state = "win"
                        else:
                            print("Bust")
                            user_state = "lose"
                        break
                    break
                else:
                    print("Please choose a defined value")

# Totals the value of the dealears hand giving it's true point value as one card is no longer hidden            
            dealer_points += card_points[dealer[-1]]

# If the dealer recived a natural blackjack imidiatly thier points are updatet acordingly         
            if dealer_points == 21:
                dealer_points = "Blackjack!"
                break
            
            print(f"\nThe dealer has a {', and a '.join(dealer)} Points: {dealer_points}. \n\nYou have a {', and a '.join(user)} Points: {user_points} \n")

# The dealer plays thier turn with a delay of an empty input to allow the user to read what has happend betwen plays
            while True:
                input("Press enter to continue")
# Checks are performed to see if the dealers turn is over or if they shoyld keep on playing 
                if dealer_points == "Blackjack!":
                    break                
                elif dealer_points >= 17: 
                    break
                elif user_points == "Blackjack!":
                    break
                elif user_points >= 21:
                    break
# the dealers hits and if nececarry the "ace_value_dealer" function is called so the appropriat amount of points is recived
                else:
                    delear_new_card = deck.pop(0)
                    dealer.append(delear_new_card)
                    dealer_points += card_points[dealer[-1]]
                    if ace_value_dealer(dealer, dealer_points, ace_dealer_test) == True:
                        dealer_points -= 10
                        ace_dealer_test = 1
                print(f"\nThe dealer has a {', and a '.join(dealer)} Points: {dealer_points}. \n\nYou have a {', and a '.join(user)} Points: {user_points} \n")

# Checks if thier has been a draw in blackjack terms a push resulting changing the "user_state" to "push"
            if user_points == dealer_points:
                print("Push!")
                user_state = "push"
                break
            
# Checks if one of the players has recived a natural "Blackjack!" then acting accordingly
# making the "user_state" either "blackjack win" or "lose" depending on who recived the natural blackjack
            elif user_points == "Blackjack!" or dealer_points == "Blackjack!":    
                if user_points == "Blackjack!":
                    print("You won with Blackjack! Congratlations!")
                    user_state = "blackjack win"
                elif dealer_points == "Blackjack!":
                    print("You lost by Blackjack! :")
                    user_state = "lose"
            
# Checks if the user has won and if so changes the "user_state" to "win"
            elif user_points > dealer_points and user_points <= 21 or dealer_points > 21:
                print("You Win!")
                user_state = "win"

# Checks if the user has lost and if so changes the "user_state to "win"
            elif dealer_points > user_points and dealer_points <= 21 or user_points > 21:
                print("You Lose")
                user_state = "lose"

# ..??                
            if user_state == "win":
                balance += bet
                print(f"You won {bet} you now have ${balance} in your account")
                break
# ..??
            elif user_state == "push":
                balance += bet
                print("You drawed with the dealer")
# ..??      
            elif user_state == "blackjack win":
                balance += int(round(bet*1.5, 1))
                print(f"You won {int(round(bet*1.5,1))} by blackjack you now have ${balance} in your account")
# ..??
            elif user_state == "lose":
                balance -= bet
                print(f"You lost ${bet} you now have ${balance} in your account")
                break
# Checks if there has been a witdraw and then the appropriat steps for the circumstances of the witdraw   
    if withdraw_state == False:
        if balance > initial_balance:
            print(f"You witdrew your balance of ${balance} for a proft of ${balance-initial_balance}")
        elif balance == initial_balance:
            print(f"You witdrew ${balance} wich is the same as you started with")
        else:
            print(f"You witdrew your balance of ${balance} for a loss of ${initial_balance-balance}")

# Incase the user runs out of money 
    else:
        print("You ran out of money. Better luck next time!")

# Let's play!
main()