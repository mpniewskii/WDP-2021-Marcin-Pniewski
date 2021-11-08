from random import seed
from random import randint
seed = (43664343265)

x = 1
n = 7
m = 10

a = []
for i in range (n):
    a.append([0]*m)

for z in a:
    for u in range (len(z)):
        z[u] = randint(0, 10)

for i in a:
    print (i)