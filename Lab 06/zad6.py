import math

liczba = input()
liczba = int(liczba)
dzielnik = 10
temp = 0
print(liczba%dzielnik)
piwo = []
dowhile = list(str(liczba))
licznik = 0

for i in dowhile:
    licznik = licznik+1

while licznik>0:
    temp = liczba % dzielnik
    piwo.append(temp)
    liczba = int(liczba/10)
    licznik = licznik-1

print(licznik)
print(dowhile)
print(piwo)
print(sum(piwo))



