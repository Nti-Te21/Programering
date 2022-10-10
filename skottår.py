år=int(input("år "))
if år % 4 == 0 and år % 100 != 0 or år % 400 == 0 :
    print(f"{år} är ett skottår")
else:
    print(f"{år} är inte ett skottår")
    