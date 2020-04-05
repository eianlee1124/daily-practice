def func(n):
    return n + sum(list(map(int, str(n))))

LIMIT = 10000
numbers = [0] * LIMIT

for i in range(LIMIT):
    n = func(i)
    if n < LIMIT:
        numbers[n] = 1

for i in range(LIMIT):
    if numbers[i] == 0:
        print(i)