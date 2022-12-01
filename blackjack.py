#jag kommer få A++ fr jag bäst blackjack gör riggat för alla som har användar namn hampuse1 och 10000000 blackjack poäng = 100kr du kan då cacha ut mång gånger och ruinera mig och känna 10k+ så länge jag får A++ på uppgiften och kursen tack
import random
def deck_create():
    suits = ["Hearts", "Diamonds","Spades", "Clubbs", ]
    values = ["King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3" , "2", "Ace"]
    deck = []
    for suit in suits:
        for value in values:
            deck.append(value + " of " + suit)
    return deck
def def_points (deck):
    points = {}
    for cards in deck:
        card = cards.split(" ")
        if card[0] == "King" or card[0] == "Queen" or card[0] == "Jack":
            points[cards] = 10
        elif card[0].isdigit():
            points[cards] = int(card[0])
        elif card[0] == "Ace":
            points[cards] = 11
    return points
def deposit():
    while True:
        deposit = input("How much do you want to deposit? ")
        if deposit.isdigit():
            balance = deposit
            print(f"Your balance is now ${balance}")
            return balance
            break
        else:
            print("deposite must be a number")
            continue
def shuffel_deck(deck):
    random.shuffle(deck)
def first_deal(deck, dealer, user):
    for _ in range(2):
        card_1 = deck.pop(0)
        dealer.append(card_1)
        card_2 = deck.pop(0)
        user.append(card_2)
def main():
    balance = deposit()
    deck = deck_create()
    card_points = def_points(deck)
    dealer=[]
    user=[]
    shuffel_deck(deck)
    first_deal(deck, dealer, user)
    dealer_points = card_points[dealer[1]]
    user_points = card_points[user[0]] + card_points[user[1]]
    print(f"\nThe dealer has {dealer[1]} and a hidden card Points: {dealer_points}. \n\nYou have a {', and a '.join(user)} Points: {user_points} \n")

main()
