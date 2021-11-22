def szukajWLiscie(lista, a):
    licznik = 0
    for i in lista:
        if i == a:
            licznik+=1
    return licznik

x = szukajWLiscie([8, 8, 1, 8, 8], 1)
print(x)