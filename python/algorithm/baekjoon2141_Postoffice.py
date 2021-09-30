# 우체국
from sys import stdin

def get_optimal_position(p):
    mid = p//2 + p%2
    balance = 0
    for pos, popul in v:
        balance += popul

        if balance >= mid:
            return pos

n = int(stdin.readline())
v = []

t = 0
for _ in range(n):
    x, a = map(int, stdin.readline().split())
    v.append((x, a))
    t += a

v.sort()
print(get_optimal_position(t))