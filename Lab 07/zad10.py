import math

def obwodzik(x, y, z):
    wynik = math.sqrt(math.pow(x[0]-y[0], 2) + math.pow(x[1]-y[1], 2))
    wynik += math.sqrt(math.pow(x[0]-z[0], 2) + math.pow(x[1]-z[1], 2))
    wynik += math.sqrt(math.pow(z[0]-y[0], 2) + math.pow(z[1]-y[1], 2))
    return wynik

print(obwodzik([7.5, -8], [-2, 0], [7, 12]))