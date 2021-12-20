import time
n = 2
i = 0
while i<30:
    print(i)
    i = i+1
    time.sleep(n)
    while n>0.1:
        n = n-0.1