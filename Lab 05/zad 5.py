from random import seed
from random import randint
seed = (43664343265)

n = 7
m = 7


a = []
for i in range (n):
    a.append([0]*m)

for z in a:
    for u in range (len(z)):
        z[u] = randint(0, 10)

for i in a:
    print (i)
x = 0
w = 0
y = 0

while x<len(a):
    w = w + a[y][x]
    print(a[y][x])
    x = x+1
    y = y+1
print(w)