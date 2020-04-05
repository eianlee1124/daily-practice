from inputs import *
load('10870')

def fib(n):
    return fib(n-1) + fib(n-2) if n >= 2 else n

n = int(input())
print(fib(n))