from inputs import *
load('3047')

numbers = sorted(map(int, input().split()))
order = input()
for i in order:
    if i == 'A':
        print(numbers[0], end=' ')
    if i == 'B':
        print(numbers[1], end=' ')
    if i == 'C':
        print(numbers[2], end=' ')