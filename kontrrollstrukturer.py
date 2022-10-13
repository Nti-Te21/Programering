def leap_year (år=int(input("år "))):
    if år % 4 == 0 and år % 100 != 0 or år % 400 == 0 :
        print(f"år {år} är ett skottår")
    else:
        print(f"år {år} är inte ett skottår")
leap_year()

def pyramid (steg= int(input("Antal steg i pyramiden "))):
    utskrift=[]
    for i in range(steg ,0 ,-1):
        utskrift.append(i)
        print(*utskrift)
pyramid()

# Login  
# Skelettkod till uppgiften

accounts = {}
logged_in = False

while True:
    menyval = input(
        "1. Skapa konto\n"
        "2. Logga in\n"
        "3. Läs en rolig historia\n"
        "4. Logga ut\n"
        "5. Avsluta program\n"
    )

    if menyval == "1":
        # TODO Skapa ett konto genom att lägga till ett key-value par i accounts
        # username = key, password = value
        # Bonus: Kolla först så att användaren inte redan finns
        username_add = input("Username: ")
        password_add = input("Password: ")
        if username_add in accounts:
            print("Username is already taken")
        else:
            accounts[username_add] = password_add

    elif menyval == "2":
        # TODO Användaren ska få logga in med username och password
        # Ändra variabeln logged_in till True om de lyckas logga in
        # Bonus: Ge användaren ett visst antal försök att logga in
        tries = 0
        while tries < 10:
            username = input("Username: ")
            password = input("Password: ")
            if username in accounts:
                if accounts[username] == password:
                    print("\nLogged in\n")
                    logged_in = True
                    break
            else:
                print("Username or Password is incorrect please try again")
                tries += 1

    elif menyval == "3":
        # TODO skriv ut en rolig historia, men bara om användaren är inloggad
        # Bonus: Skriv ut en tråkig historia om de inte är inloggade
        if logged_in == True:
            print("\n Once upon a time there was a funny story.\n It was so funny everyone laughed as they where reminded of it after hearing it once.\n It was actually mostly a joke question.\n It read: Would you rather have Unlimited bacon but no games or games UNLIMITED games but no games?\n")
        else:
            print("\n Once there was a boring story of a person who wasent logged in.\n So log in now and then you can read a funnier story.\n")

    elif menyval == "4":
        # TODO Ändra variabeln logged_in till False
        # Bonus: Fråga om de är säkra först
        if logged_in == True:
            logout = input("Are you sure? ").capitalize()
            print(logout)
            if logout == "Yes":
                logged_in = False
                print("You logged out")
        else:
            print("You're not logged in")

    elif menyval == "5":
        break

import random
tal = random.randint(1,100)
gissning = None
while gissning != tal:
    gissning = int(input ("Vilket tal tänker jag på? "))
    if gissning < tal:
        print("högre!")
    elif gissning > tal:
        print("lägre!")
print(f"Bravo du gissade rätt jag tänkte på talet {tal}!")