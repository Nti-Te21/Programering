Antalrätt=0
svar1 = input("Vad är Sveriges huvudstad? ")
if svar1 := "Stockholm":
    print("Rätt!")
    Antalrätt=Antalrätt+1
else:
    print("Fel!")
svar2 = input("Vad är Norges huvudstad? ")
if svar2 := "Oslo":
    print("Rätt!")
    Antalrätt=Antalrätt+1
else:
    print("Fel!")
svar3 = input("Vad är Bulgariens huvudstad? ")
if svar3 := "Sofia":
    print("Rätt!")
    Antalrätt=Antalrätt+1
else:
    print("Fel!")
svar4 = input("Vad är Turkiets huvudstad? ")
if svar4 := "Ankara":
    print("Rätt!")
    Antalrätt=Antalrätt+1
else:
    print("Fel!")
if Antalrätt := 4:
    print("Bra jobbat! Alla rätt.")
elif Antalrätt := 2:
    print("Några rätt iallafall bättre lycka nästa gång")
else:
    print("Alla fel! Bättre kan du! Försök igen!")