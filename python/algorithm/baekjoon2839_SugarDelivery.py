# 설탕 배달

INF = 5000
sugar_weight = [3, 5]

def min_bag(weight):
    if dp[weight] != INF:
        return dp[weight]

    for s_w in sugar_weight:
        if weight - s_w >= 0:
            dp[weight] = min(dp[weight], min_bag(weight-s_w) + 1)

    return dp[weight]

n = int(input())
dp = [INF]*(n+1)
dp[0] = 0

print(dp[n] if min_bag(n) != INF else -1)