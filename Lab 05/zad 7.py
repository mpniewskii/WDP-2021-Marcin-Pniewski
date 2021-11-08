from random import seed
from random import randint

seed = (43664343265)

n = 2
m = 3
x = 0
temp = []

a = []
for i in range (n):
    a.append([0]*m)

for z in a:
    for u in range (len(z)):
        z[u] = randint(0, 10)

for i in a:
    print (i)

for i in range(len(a[0])):
    temp.append([])
    for c in range (len(a)):
        temp[i].append(a[c][i])
print(temp)

