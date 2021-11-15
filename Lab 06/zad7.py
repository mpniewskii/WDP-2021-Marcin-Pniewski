import math

liczba = int(input())
wyniczek = []
temp = 0

while liczba>0:
    temp = liczba % 2
    wyniczek.append(temp)
    liczba = liczba // 2
    print(liczba)

print(wyniczek)
print(wyniczek[::-1])
