def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-2)+fib(n-1)
print(fib(5))
print(fib(6))
print(fib(10))
