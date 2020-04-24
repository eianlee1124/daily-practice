def solution(arr, divisor):
    return sorted(n for n in arr if n % divisor == 0) or [-1]

if __name__ == "__main__":
    print(solution([5,9,7,10], 5))