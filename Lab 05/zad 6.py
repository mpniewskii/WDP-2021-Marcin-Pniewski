from random import seed
from random import randint
seed = (43664343265)

n = 7
m = 7
k = 0
temp = []

a = []
for i in range (n):
    a.append([0]*m)

for z in a:
    for u in range (len(z)):
        z[u] = randint(0, 10)


x = 0
y = 0

while x<len(a):
    for z in a:
        x = x + 1
        for u in range (x):
            z[u] = 0


for i in a:
    temp.append(sum(i))
print(sum(temp))