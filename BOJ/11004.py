from inputs import *
load('11004')

N, K = map(int, input().split())
A = sorted(map(int, input().split()))
print(A[K-1])