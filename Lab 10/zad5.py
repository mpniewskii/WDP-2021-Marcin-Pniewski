towar = [{'nazwa': 'banan', 'jednostka': 'kg', 'ilosc': 10, 'cena': 3},
         {'nazwa': 'jablko', 'jednostka': 'kg', 'ilosc': 16, 'cena': 2.5},
         {'nazwa': 'maka pszenna', 'jednostka': 'op.', 'ilosc': 30, 'cena': 2.5},
         {'nazwa': 'mydlo', 'jednostka': 'szt.', 'ilosc': 6, 'cena': 1.5},
         {'nazwa': 'jogurt naturalny', 'jednostka': 'szt.', 'ilosc': 20, 'cena': 1.5},
         {'nazwa': 'papier toaletowy 8 rolek', 'jednostka': 'op.', 'ilosc': 10, 'cena': 9}]
def wyszukaj(towar, nazwa):
    for i in towar:
        if i['nazwa'] == nazwa:
            print(i)
def sumuj(towar, nazwa):
    for i in towar:
        if i['nazwa'] == nazwa:
            print(i['ilosc']*i['cena'])

def sumujWszystko(towar):
    z = []
    for i in towar:
        z.append(i['ilosc'] * i['cena'])
    print(sum(z))
def dodajTowar(towar, nazwa, jednostka, ilosc, cena):
    towar.append({'nazwa': nazwa, 'jednostka': jednostka, 'ilosc': ilosc, 'cena': cena})
    for i in towar:
        print(i)

def aktualizujIlosc(towar, nazwa, ilosc):
    for i in towar:
        if i['nazwa'] == nazwa:
            i['ilosc'] = i['ilosc']+ilosc
            for i in towar:
                print(i)

def filtrJednostka(towar, jednostka):
    for i in towar:
        if i['jednostka'] == jednostka:
            print(i['nazwa'])


wyszukaj(towar, 'jablko')
sumuj(towar, 'mydlo')
sumujWszystko(towar)
dodajTowar(towar, 'pomidorki', 'kg', 55, 2)
aktualizujIlosc(towar, 'jablko', 4)
filtrJednostka(towar, 'kg')

