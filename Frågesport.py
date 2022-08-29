Antalrätt=0
svar1 = input("Vad är Sveriges huvudstad? ").capitalize()
if svar1 == "Stockholm":
    print("Rätt!")
    Antalrätt=Antalrätt+1
else:
    print("Fel!")
svar2 = input("Vad är Norges huvudstad? ").capitalize()
if svar2 == "Oslo":
    print("Rätt!")
    Antalrätt=Antalrätt+1
else:
    print("Fel!")
svar3 = input("Vad är Bulgariens huvudstad? ").capitalize()
if svar3 == "Sofia":
    print("Rätt!")
    Antalrätt=Antalrätt+1
else:
    print("Fel!")
svar4 = input("Vad är Turkiets huvudstad? ").capitalize()
if svar4 == "Ankara":
    print("Rätt!")
    Antalrätt=Antalrätt+1
else:
    print("Fel!")
if Antalrätt == 4:
    print("Bra jobbat! Alla rätt 4/4.")
elif Antalrätt == 1 or Antalrätt == 2 or Antalrätt == 3:
    print(f"Några rätt iallafall bättre lycka nästa gång {Antalrätt}/4")
else:
    print("Alla fel! Bättre kan du! Försök igen!")