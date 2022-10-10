# Övning 4 går ut på att implementera så många av nedanstående funktioner som möjligt
# Ta bort pass och implementera funktionerna


from unicodedata import name


def best(name):
    # TODO Skriv ut att namnet är bäst
    # Ex: "Katherine" in - skriver ut "Katherine är bäst"
    print(f" {name} är det bästa namnet")

best(input("Name "))
def square(knumer):
    # TODO Returnera talet kvadrerat
    # Ex: 5 in - 25 ut
    return(knumer**2)
sq_svar = square(int(input("tal ")))
print(sq_svar)
def sums(sumeringslista):
    # TODO Returnera summan av a och b
    # Ex: 2, 6 in - 8 ut
    numbers = list(map(int, sumeringslista.split(" ")))
    summa1=0
    for number in numbers:
        summa1 += number
    return(summa1)
svarsum = sums(sumeringslista = input("två tal "))
print(svarsum)


# Nu blir det lite svårare


def maximum(talen):
    # TODO Returnera det största av a,b,c
    # Ex: 3, 6, 12 in - 12 ut
    max_tal =  0
    for tal in (talen):
        if int(tal)> max_tal:
            max_tal = int(tal)
    return(max_tal)
max_tal = maximum(talen = input("en mängd tal ").split(" "))
print(f"det störst talet är {max_tal}")

def palindrom(testord):
    # TODO Returnera True om ord är ett palindrom
    # Ex: abba in - True ut
    # Palindrom är ett ord som stavas likadant baklänges och framlänges.
    jämförelse = testord[::-1]
    if testord == jämförelse:
        return True
    else:
        return False
palindrom(testord = input("skriv ett möjligt palindrom "))

def primtal():
    # TODO Returnera True om nr är ett primtal, annars returnera false
    # Ex: 5 in - True ut
    testtal = int(input("ett potentiellt primtal "))
    for i in range(2,testtal):
        if testtal%i == 0:
            return False
    return True
prim = primtal()
print(prim)

