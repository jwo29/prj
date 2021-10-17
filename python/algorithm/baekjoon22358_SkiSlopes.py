# 스키장
from sys import stdin
from collections import defaultdict

N, M, K, S, T = map(int, input().split())
courses = defaultdict(list)
lift = decimal(list)

for _ in range(M):
    a, b, t = map(int, stdin.readline().split())
    courses[a].append((b, t))
    lift[a].append(b) # 도착지점이 a가 되는 코스 b들
