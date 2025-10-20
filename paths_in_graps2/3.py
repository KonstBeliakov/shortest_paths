# money exchange
n, m = map(int, input().split())
edges = [[int(i) for i in input().split()] for _ in range(m)]
adj = [[] for _ in range(n + 1)]
for e in edges:
    adj[e[0]].append((e[1], e[2]))
u = int(input())

inf = 10**9
dist = [inf] * (n+1)
prev = [None] * (n+1)
dist[u] = 0
for i in range(m - 1):
    for (v1, v2, cost) in edges:
        dist[v2] = min(dist[v2], dist[v1] + cost)
        prev[v2] = v1

# Checking for negative cycles
for (v1, v2, cost) in edges:
    if(dist[v2] > dist[v1] + cost):
        dist[v2] = -inf

for i in range(1, n + 1):
    if dist[i] == inf:
        print("*")
    elif dist[i] == -inf:
        print("-")
    else:
        print(dist[i])
