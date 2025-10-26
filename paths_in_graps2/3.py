# money exchange
n, m = map(int, input().split())
edges = [[int(i) for i in input().split()] for _ in range(m)]
adj = [[] for _ in range(n + 1)]
for e in edges:
    adj[e[0]].append((e[1], e[2]))
u = int(input())

inf = 10**9
dist = [inf] * (n+1)
dist[u] = 0
for i in range(m - 1):
    for (v1, v2, cost) in edges:
        if  dist[v1] != inf and dist[v2] > dist[v1] + cost:
            dist[v2] = dist[v1] + cost

# Checking for negative cycles
neg_cycles = [False] * (n+1)
for (v1, v2, cost) in edges:
    if dist[v1] != inf and dist[v2] > dist[v1] + cost:
        neg_cycles[v2] = True

for i in range(m - 1):
    for (v1, v2, _) in edges:
        if neg_cycles[v1]:
            neg_cycles[v2] = True

for i in range(1, n + 1):
    if dist[i] == inf:
        print("*")
    elif neg_cycles[i]:
        print("-")
    else:
        print(dist[i])
