# Desert Cafe
from sys import stdin
from collections import defaultdict

INF = 1001

def find_good_place():
    for apartment in apartments:

        distance = [1001] * (n+1)
        distance[apartment] = 0

        nearest_adj, shortest_dist = 0, 1001
        for adj, dist in town[apartment]:
            if dist == shortest_dist: # shortest가 중복되는 경우
                nearest_adj = 0
                break
            if dist < shortest_dist:
                nearest_adj = adj
                shortest_dist = dist

        isGoodPlace[apartment] = True
        isGoodPlace[nearest_adj] = True

n, k = map(int, stdin.readline().split())
isGoodPlace = [False] * (n+1)
town = defaultdict(list)
cnt = 0

for _ in range(n-1):
    i, j, w = map(int, stdin.readline().split())
    town[i].append((j, w))
    town[j].append((i, w))

apartments = list(map(int, stdin.readline().split()))
find_good_place()

for i in range(1, n+1):
    if isGoodPlace[i]:
        cnt += 1

print(cnt)
