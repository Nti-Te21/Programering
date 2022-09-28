from __future__ import absolute_import


def best_city():
    city = input("Solna ")
    city = "Solna"
    print(f"Den bästa staden är {city}")

best_city()

def number_1():

    number = int(input("number+1 "))
    print(number+1)

number_1()

def absolutvärde():
    numer = int(input("numer absolut värde "))
    print(abs(numer))
absolutvärde()

def square(knumer):
    print(knumer**2)
square(int(input("tal att kvadrera ")))

def summa(sumeringslista):
    numbers = list(map(int, sumeringslista.split(" ")))
    summa1=0
    for number in numbers:
        summa1 += number
    print(summa1)

summa(sumeringslista = input("två tal "))


def max():
    max_tal =  0
    talen = input("tre tal ").split(" ")
    for tal in (talen):
        if int(tal)> max_tal:
            max_tal = int(tal)
    print(f"det störst talet är {max_tal}")

max()

def summa_list():
    lista = input("tal att summera ").split (" ")
    lista = [int(x) for x in lista]
    Summa = sum(lista)
    print(Summa)

summa_list()


def unik_tal():
    uniktal=input("tal med upprepning av minst ett tal ").split(" ")
    unikset = set(uniktal)
    print(*unikset)

unik_tal()

# med stackoverflow är allt möjligt och det mesta lätt
def palindrom():
    testord = input("skriv ett möjligt palindrom ")
    jämförelse = testord[::-1]
    if testord == jämförelse:
        print(f"Testordet {testord} är ett palindrom")
    else:
        print(f"Testordet {testord} är inte ett palindrom utan är {jämförelse} backlänges")
palindrom()