# N과 M (1)
def dfs(length):
    if length == m:
        print(*selected)
    else:
        for i in range(1, n+1):
            if not visited[i]:
                visited[i] = True
                selected.append(i)
                dfs(length+1)
                visited[i] = False
                selected.pop()

n, m = map(int, input().split())
selected = list()
visited = [False for _ in range(n+1)]

dfs(0)