#!/usr/bin/env python3


def solution(arr1, arr2):
    answer = []
    N, M = map(len, [arr1, arr1[0]])
    for i in range(N):
        temp = []
        for j in range(M):
           temp.append(arr1[i][j] + arr2[i][j])
        answer.append(temp)
    return answer


if __name__ == "__main__":
    print(solution([[1,2], [2,3]], [[3,4], [5,6]]))
    print(solution([[1],[2]], [[3], [4]]))
