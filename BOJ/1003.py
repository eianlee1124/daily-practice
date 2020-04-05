from inputs import *
load('1003')

def fib(n):
    cache = (
        (1, 0),
        (0, 1),
        (1, 1)
    )
    if n < 3:
        return cache[n]
    
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a + b
    return a, b

test = int(input())
for _ in range(test):
    n = int(input())
    print(*fib(n))