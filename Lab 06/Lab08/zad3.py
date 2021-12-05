def kafle(x, y):
    if x == 1:
        return y
    else:
        return x*x*kafle(1, y)

print(kafle(3, 6))