def binarka(n):
    if n==1:
        return 1
    else:
        return str(binarka(n//2)) + str(n%2)



print(binarka(2))