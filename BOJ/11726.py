from inputs import *
load('11726')

x, y = 1, 1
for _ in range(int(input())):
    x, y = y, x + y

print(x % 10007)

