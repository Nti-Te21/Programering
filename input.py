name = input("Vad heter du? ")
print("Välkommen tillbaka", name)
age = int(input ("Hur gammal är du? "))
print(name,age)
age30 = 30 - age
if age30 >= 0:
    print(" Visste du att om", age30, "år är du 30 år gammal?" )
else:
    print("Du är redan över 30 år gammal :(")

