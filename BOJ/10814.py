from inputs import *
load('10814')

N = int(input())
ret = sorted((tuple(input().split()) for _ in range(N)), key=lambda x: int(x[0]))
for age, name in ret:
    print(age, name)