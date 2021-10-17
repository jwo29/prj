# 피보나치 수 5
n = int(input())

if n < 2:
    print(n)
else:
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])

    print(dp[n])