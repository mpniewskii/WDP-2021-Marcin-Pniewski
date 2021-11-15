from random import seed
from random import randint
seed = (420)
losowana = randint(0, 100)
licznik = 0
print(losowana) #Dla potrzeb sprawdzajacego!

while True:
    zgadniecie = input()
    zgadniecie = int(zgadniecie)
    if zgadniecie>losowana:
        print("liczba za duza")
    if zgadniecie<losowana:
        print("liczba za mala")
    licznik += 1
    if zgadniecie == losowana:
        print("Gratulacje zgadles, liczba twoich strzalow to:", licznik)
