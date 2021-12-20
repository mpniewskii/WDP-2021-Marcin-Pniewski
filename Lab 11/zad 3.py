plik = open("miasta.csv", 'r')
plik2 = open('liczby.txt', 'w')


for i in range(1, 101):
    i = str(i)
    plik2.write(i+'\n')
plik2.close()
plik3 = open('liczby.txt', 'r')
for i in plik3:
    print(i)
plik3.close()

testowe = open('liczby.txt', 'w')
for i in testowe:
    temp = 0
    temp = int(i)
    if temp%2 == 0:
        temp = temp+10
        temp = str(temp)
        i = temp

for i in testowe:
    print(i)