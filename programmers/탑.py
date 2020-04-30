#!/usr/bin/env python3


from itertools import permutations

def solution(heights):
    n = len(heights)
    recv = [0] * n
    
    for i in range(n-1, 0, -1):
        for j in range(i-1, -1, -1):
            if heights[i] < heights[j]:
                recv[i] = j+1
                break
    
    return recv


if __name__ == "__main__":
    print(solution([6,9,5,7,4]))
    print(solution([3,9,9,3,5,7,2]))
