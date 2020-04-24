from inputs import *
load('10989')

N = int(input())
numbers = [0] * 10001


for _ in range(N):
    numbers[int(sys.stdin.readline())] += 1
    
for i in range(len(numbers)):
    sys.stdout.write('%s\n' % i * numbers[i])