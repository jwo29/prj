# 가장 긴 증가하는 부분 수열
from sys import stdin

n = int(input())
a = list(map(int, stdin.readline().split()))

if n < 2:
    print(1)
else:
    dp = [0]*n
    dp[0] = 1

    for i in range(1, n):
        dp[i] = dp[i-1]
        if a[i] > a[i-1] and a[i]:
            dp[i] += 1

    print(dp[-1])