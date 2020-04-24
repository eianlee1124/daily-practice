def solution(arr):
    answer = [arr[0]]
    
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
            
    return answer
    
if __name__ == "__main__":
    print(solution([1,1,3,3,0,1,1]))