import math

labirynt = [[1, 1, 1, 1, 1, 1, 1], [1, 2, 1, 0, 0, 0, 1], [1, 0, 1, 0, 1, 1, 1], [1, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 1, 3, 1], [1, 1, 1, 1, 1, 1, 1]]
wynik = 0

def rysujLabirynt(labirynt, puste, sciana, ludzik, drzwi):
    liczniki = 0
    labirynt1 = []
    for i in labirynt:
        liczniki += 1
        licznikx = 0
        druk = []
        for x in i:
            if x == 0:
                druk.append(puste)
            elif x == 2:
                druk.append(ludzik)
            elif x == 1:
                druk.append(sciana)
            elif x == 3:
                druk.append(drzwi)
        labirynt1.append(druk)
    return labirynt1

def aktualizujLabirynt(labirynt, tempruch):
    wx = 1
    wy = 1
    if tempruch == 's' and labirynt[wx+1][wy] != 1:
        labirynt[wx][wy] = 0
        wx = wx+1
        labirynt[wx][wy] = 2
        return rysujLabirynt(labirynt, " ", "#", "@", "o")
    elif tempruch == 'w' and labirynt[wx-1][wy] != 1:
        labirynt[wx][wy] = 0
        wx = wx-1
        labirynt[wx][wy] = 2
        return rysujLabirynt(labirynt, " ", "#", "@", "o")
    elif tempruch == 'a' and labirynt[wx][wy - 1] != 1:
        labirynt[wx][wy] = 0
        wy = wy-1
        labirynt[wx][wy] = 2
        return rysujLabirynt(labirynt, " ", "#", "@", "o")
    elif tempruch == 'd' and labirynt[wx][wy+1] != 1:
        labirynt[wx][wy] = 0
        wy = wy +1
        labirynt[wx][wy] = 2
        return rysujLabirynt(labirynt, " ", "#", "@", "o")

def gra(labirynt, ruchy):
    while ruchy>0:
        tempruch = input()
        return aktualizujLabirynt(labirynt, tempruch)

x = rysujLabirynt(labirynt, " ", "#", "@", "o")
y = aktualizujLabirynt(labirynt, 's')
z = gra(labirynt, 5)
for i in x:
    print(i)
for i in y:
    print(i)
