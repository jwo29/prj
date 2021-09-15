# 빠른 A+B
from sys import stdin

n = int(input())

for _ in range(n):
    a, b = map(int, stdin.readline().split())
    print(a+b)