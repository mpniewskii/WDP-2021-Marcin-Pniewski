import time

start = time.time()



labirynt = [[1, 1, 1, 1, 1, 1, 1], [1, 2, 1, 0, 0, 0, 1], [1, 0, 1, 0, 1, 1, 1], [1, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 1, 3, 1], [1, 1, 1, 1, 1, 1, 1]]
ruchy = 0
x = 1
y = 1



for i in labirynt:
    print(i)

while labirynt[5][5] == 3 and ruchy < 20:
    print("Podaj ruch")
    tempruch = input()
    if tempruch == 's' and labirynt[x+1][y] != 1:
        labirynt[x][y] = 0
        x = x+1
        labirynt[x][y] = 2
        ruchy += 1
        for i in labirynt:
            print(i)
    if tempruch == 'w' and labirynt[x-1][y] != 1:
        labirynt[x][y] = 0
        x = x-1
        labirynt[x][y] = 2
        ruchy += 1
        for i in labirynt:
            print(i)
    if tempruch == 'a' and labirynt[x][y-1] != 1:
        labirynt[x][y] = 0
        y = y-1
        labirynt[x][y] = 2
        ruchy += 1
        for i in labirynt:
            print(i)
    if tempruch == 'd' and labirynt[x][y+1] != 1:
        labirynt[x][y] = 0
        y = y+1
        labirynt[x][y] = 2
        ruchy += 1
        for i in labirynt:
            print(i)


end = time.time()
print(end-start)