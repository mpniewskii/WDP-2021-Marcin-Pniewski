import math

def odleglosc(x, y):
    wynik = math.sqrt(math.pow(x[0]-y[0], 2) + math.pow(x[1]-y[1], 2))
    return wynik

x = odleglosc([7.5, -8], [-2, 0])
print(x)