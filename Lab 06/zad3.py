import math
def pierwsza(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    pierw = int(n**0.5) + 1
    for dzielnik in range(3, pierw, 2):
        if n % dzielnik == 0:
            return False
    return True

liczba = input()
liczba = int(liczba)
n = 1
suma = 0
piwo = []
licznik = 0


while n < liczba:
    if pierwsza(n):
        piwo.append(n)
        licznik = licznik +1
    suma = suma+n
    n = n+1

print(piwo)
print(licznik)