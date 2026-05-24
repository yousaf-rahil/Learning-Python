def fectorial(n):
    if n ==0 or n == 1:
        return 1
    else:
        return n * fectorial(n-1)
    
def fib(n):
    if n ==0 or n ==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fectorial(6))
print(fib(8))