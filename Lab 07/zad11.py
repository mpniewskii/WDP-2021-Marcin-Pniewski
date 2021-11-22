import math


def linia(x, y, z):
    if (y[1] - x[1]) / (y[0] - x[0]) == (z[1] - x[1]) / (z[0] - x[0]) and (y[1] - z[1]) / (y[0] - z[0]) == (
            z[1] - x[1]) / (z[0] - x[0]):
        return True
    else:
        return False

def obwodzik(x, y, z):
    if linia(x, y, z) == False:
        wynik = math.sqrt(math.pow(x[0]-y[0], 2) + math.pow(x[1]-y[1], 2))
        wynik += math.sqrt(math.pow(x[0]-z[0], 2) + math.pow(x[1]-z[1], 2))
        wynik += math.sqrt(math.pow(z[0]-y[0], 2) + math.pow(z[1]-y[1], 2))
        return wynik
    else:
        print("NIE DZIALA Z POWODU TEGO WSPOLLINIOWEGO!!!!!!")
        return 0
print(obwodzik([-5, -3], [0, -1], [10, 3]))
print(obwodzik([7.5, -8], [-2, 0], [7, 12]))


