def solution(answers):
    patterns = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    
    scores = [0] * len(patterns)
    
    for i, answer in enumerate(answers):
        for j, value in enumerate(patterns):
            if answer == value[i % len(value)]:
                scores[j] += 1
    return [i+1 for i, v in enumerate(scores) if v == max(scores)]
            


    
if __name__ == "__main__":
    print(solution([1,2,3,4,5])) # return [1]
    print(solution([1,3,2,4,2])) # return [1,2,3]: