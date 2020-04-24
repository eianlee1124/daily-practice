def solution(n, lost, reserve):
    lost, reserve = map(set, [lost, reserve])
    lost, reserve = lost - reserve, reserve - lost
    
    for r in reserve:
        if r-1 in lost:
            lost.remove(r-1)
        elif r+1 in lost:
            lost.remove(r+1)
            
    return n - len(lost)

if __name__ == "__main__":
    print(solution(5, [2,4], [1,3,5])) # return 5
    print(solution(5, [2,4], [3])) # return 4
    print(solution(3, [3], [1])) # return 2