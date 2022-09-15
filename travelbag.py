travelbag = []

while True:

   menyval = input("\n1. Kolla i resväskan\n"
                   "2. Lägg sak i resväskan\n"
                   "3. Ta bort sak i resväskan\n"
                   "4. Avsluta program ")
   if menyval == "1":
    travelbag.sort()
    for i,sak in enumerate(travelbag, start=1):
        print (i, sak)

   elif menyval == "2":
       nya_saker = input("Lägg till en till sak ").split(" ")
       travelbag+= nya_saker

   elif menyval == "3":
       ta_bort = input("Vad vill du ta bort? ")
       if ta_bort in travelbag:
          travelbag.remove(ta_bort)
       elif int(ta_bort.isdigit()):
        travelbag.pop(int(ta_bort)-1)
       else:
        print("inte i resväskan")
    
   elif menyval == "4":
       break