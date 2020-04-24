from inputs import *
load('1181')
N = int(input())

words = set()

for _ in range(N):
    word = input()
    count = len(word)
    words.add((word, count))

for word, _ in sorted(words, key=lambda x: (x[1], x[0])):
    print(word)