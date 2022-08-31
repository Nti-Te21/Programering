Antalrätt = 0
Antalfrågor = 0
poäng = 0
name = input("Vad heter du?")
svårighetsgrad = input("lätt eller svårt?").capitalize()
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
    elif poäng == [1,2,3,4]:
        print(f"Några poäng iallafall. Bättre lycka nästa gång {name} {poäng}/5 poäng")
    else:
        print(f"")
else:
    print("Du har valt lätt")
    svar1 = input("Vad är Sveriges huvudstad? ").capitalize()
    if svar1 == "Stockholm":
        print("Rätt!")
        Antalrätt += 1
    else:
        print("Fel!")
    svar2 = input("Vad är Norges huvudstad? ").capitalize()
    if svar2 == "Oslo":
        print("Rätt!")
        Antalrätt += 1
    else:
      print("Fel!")
    svar3 = input("Vad är Bulgariens huvudstad? ").capitalize()
    if svar3 == "Sofia":
        print("Rätt!")
        Antalrätt += 1
    else:
     print("Fel!")
    svar4 = input("Vad är Turkiets huvudstad? ").capitalize()
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