#!/usr/bin/env python3


MOD = 1000000007

def solution(n, money):
    dp = [0] * (n+1)
    dp[0] = 1

    for m in money:
        for i in range(m, n+1):
            dp[i] += dp[i-m]

    return dp[n] % MOD
   


if __name__ == "__main__":
    print(solution(5, [1,2,5]))
