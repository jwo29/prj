# 트리의 지름
from sys import stdin

def dfs(node):
    if node not in parents: # 리프노드인 경우
        return weights[node]
    else:
        global max_diameter

        child_diameter = 0
        larger_weight = 0
        for c in parents[node]:
            child_weight = dfs(c)
            child_diameter += child_weight
            larger_weight = max(larger_weight, child_weight)

        max_diameter = max(max_diameter, child_diameter)

        return weights[node] + larger_weight

max_diameter = 0

n = int(input())
parents = dict()
weights = [0]*(n+1)

for _ in range(n-1):
    p, c, w = map(int, stdin.readline().split())
    if p not in parents:
        parents[p] = list()
    parents[p].append(c)
    weights[c] = w

dfs(1)
print(max_diameter)