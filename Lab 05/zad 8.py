from random import seed
from random import randint
seed = (43664343265)

n = 3
m = 5


a = []
for i in range (n):
    a.append([0]*m)

for z in a:
    for u in range (len(z)):
        z[u] = randint(0, 10)

for i in a:
    print (i)
x = 0

n2 = 5
m2 = 4


b = []
for i in range (n2):
    b.append([0]*m2)

for z in b:
    for u in range (len(z)):
        z[u] = randint(0, 10)

for i in b:
    print (i)

