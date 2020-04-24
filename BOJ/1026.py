from inputs import *
load('1026')


input = sys.stdin.readline
N = int(input())
A, B = [list(map(int, input().split())) for _ in range(2)]

print(sum([a*b for a, b in zip(sorted(A), sorted(B, reverse=True))]))