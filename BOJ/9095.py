from inputs import *
load('9095')

def add(n):
    if n <= 3:
        if n == 3:
            return n + 1
        return n
    return add(n-1) + add(n-2) + add(n-3)

test = int(input())

for _ in range(test):
    answer = add(int(input()))
    print(answer)
