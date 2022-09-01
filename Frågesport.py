from urllib.parse import non_hierarchical

Antalrätt = 0
Antalfrågor = 0
poäng = 0
name = input("Vad heter du? ")
svårighetsgrad = input("lätt eller svårt? ").capitalize()
if svårighetsgrad == "Svårt":
    print("Du har valt Svårt")
    ans1 = input("Vad är Azerbajdzjan huvudstad? ").capitalize()
    if ans1 == "Baku":
        print("Rätt! +1 poäng")
        poäng += 1
    else:
        print("Fel! -1 poäng")
        poäng -= 1
    ans2 = input("Vad är Sri lankas huvudstad? ").capitalize()
    if ans2 == "Colombo":
        print("Rätt! +1 poäng")
        poäng += 1
    else:
        print("Fel! -1 poäng")
        poäng -= 1
    ans3 = input("Vad är Namibias huvudstad? ").capitalize()
    if ans3 == "Windhoek":
        print("Rätt! +1 poäng")
        poäng += 1
    else:
        print("Fel! -1 poäng")
        poäng -= 1
    ans4 = input("Vad är Jemens huvudstad? ").capitalize()
    if ans4 == "Sanaa":
        print("Rätt! +2 poäng")
        poäng += 2
    else:
        print("Fel! -1 poäng")
        poäng -= 1
    if poäng == 5:
        print(f"Bra jobbat {name}! Du fick 5/5 poäng")
    elif poäng in [1,2,3,4]:
        print(f"Några poäng iallafall. Bättre lycka nästa gång {name} {poäng}/5 poäng")
    elif poäng in [0,-1,-2,-3]:
        print(f"Inte alla fel iallfall {name} prova igen eller gå tillbaks till lätt läge  sålänge")
    else:
        print(f"{name} din idiot gå tillbaka till lätt innan du skämmer ut dig mer ")
else:

    print("Du har valt lätt")
    svar1 = None
    tries = 0
    while svar1 != "Stockholm" and tries < 10:
        svar1 = input("Vad är Sveriges huvudstad? ").capitalize()
        tries += 1
    if svar1 == "Stockholm":
        print("Rätt!")
        Antalrätt += 1
    else:   
        print("Fel!")
    svar2 = None
    tries = 0
    while svar2 != "Oslo" and tries < 10:
        svar2 = input("Vad är Norges huvudstad? ").capitalize()
        tries += 1
    if svar2 == "Oslo":
        print("Rätt!")
        Antalrätt += 1
    else:
      print("Fel!")
    svar3 = None
    tries = 0
    while svar3 != "Sofia" and tries < 10 :
        svar3 = input("Vad är Bulgariens huvudstad? ").capitalize()
        tries += 1
    if svar3 == "Sofia":
        print("Rätt!")
        Antalrätt += 1
    else:
     print("Fel!")
    svar4 = None
    tries = 0
    while svar4 != "Ankara" and tries < 10:
        svar4 = input("Vad är Turkiets huvudstad? ").capitalize()
        tries += 1
    if svar4 == "Ankara":
        print("Rätt!")
        Antalrätt += 1
    else:
        print("Fel!")
    if Antalrätt == 4:
        print(f"Bra jobbat {name}! Alla rätt {Antalrätt}/4.")
    elif Antalrätt == 1 or Antalrätt == 2 or Antalrätt == 3:
        print(f"Några rätt iallafall. Bättre lycka nästa gång {name} {Antalrätt}/4")
    else:
        print(f"Alla fel! Bättre kan du {name}! Försök igen!")
print("If you want to play again rerun the program")