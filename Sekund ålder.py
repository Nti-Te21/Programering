name = input("Vad heter du?")
year = int(input(f"Hej {name} hur gammal är du?"))
month = int(input("Hur många månader är det sen din födelsedag?"))
monthage = year*12 + month 
print(monthage)
print (year, month)
int(monthage)
secage = monthage*30*24*60*60
input(f"Visste du att du är {secage} sekunder gammal?")