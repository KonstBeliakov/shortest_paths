n, m = map(int, input().split())
edges = [[int(i) for i in input().split()] for _ in range(m)]
adj = [[] for _ in range(n + 1)]
for e in edges:
    adj[e[0]].append((e[1], e[2]))

inf = 10**9
dist = [inf] * (n + 1)
dist[1] = 0
for _ in range(m-1):
    for (u, v, cost) in edges:
        dist[v] = min(dist[v], dist[u] + cost)


# Check if we still can improve some dist
print(int(
    any([dist[v] > dist[u] + cost for (u, v, cost) in edges])
))

