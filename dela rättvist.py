pers = int(input("Hur många ska dela på objekten? "))
objekt = int(input("Hur många är objekten? "))
objektvar = objekt//pers
resterande = objekt % pers
if resterande > 0:
    print(f"Alla får {objektvar} objekt var och det blir {resterande} objekt över")
else:
    print(f"Alla får {objektvar} objekt var")