liczba = int(input("Podaj liczbe dodatnia:"))

i = 1
suma = 0

while i <= liczba:
    suma = suma + i
    i += 1

wynik = "costam costam {} dalej costam elo {}"
wynik = wynik.format(liczba, suma)
print(wynik)