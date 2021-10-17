# 신나는 함수 실행
from sys import stdin

INF = 100000

def w(a, b, c):
    if dp[a][b][c] != INF:
        return dp[a][b][c]

    if a <= b or b <= 0 or c <= 0:
        dp[a][b][c] = 1
    if a > 20 or b > 20 or c > 20:
        dp[a][b][c] = w(20, 20, 20)
    if a < b and b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

    return dp[a][b][c]

dp = [[[INF for _ in range(100)] for _ in range(100)] for _ in range(100)]

while True:
    a_value, b_value, c_value = map(int, stdin.readline().split())

    if a_value == -1 and b_value == -1 and c_value == -1:
        break
    else:
        print(f'w({a_value}, {b_value}, {c_value}) = {w(a_value, b_value, c_value)}')
