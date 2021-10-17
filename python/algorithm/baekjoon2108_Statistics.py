# 통계학
n = int(input())
freq = dict()
arr = list()
max_freq = 0

for _ in range(n):
    v = int(input())
    arr.append(v)
    if v not in freq:
        freq[v] = 0
    freq[v] += 1

for f in freq:


arr.sort()

ans = [round(sum(arr)/n), arr[n/2], ]