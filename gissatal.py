import random
tal = random.randint(1,5000)
gissning = None
while gissning != tal:
    gissning = int(input ("Vilket tal tänker jag på? "))
    if gissning < tal:
        print("högre!")
    elif gissning > tal:
        print("lägre!")
print(f"Bravo du gissade rätt jag tänkte på talet {tal}!")
