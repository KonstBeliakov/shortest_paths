n, m = map(int, input().split())
edges = [[int(i) for i in input().split()] for _ in range(m)]
adj = [[] for _ in range(n + 1)]
for e in edges:
    adj[e[0]].append(e[1])
    adj[e[1]].append(e[0])
u, v = map(int, input().split())
inf = 10**9
dist = [inf for _ in range(n + 1)]
dist[u] = 0
nodes = {u}
while nodes:
    new_nodes = set()
    for n in nodes:
        for neighbor in adj[n]:
            if dist[neighbor] > dist[n] + 1:
                dist[neighbor] = dist[n] + 1
                new_nodes.add(neighbor)
    nodes = new_nodes
print(dist[v] if dist[v] < inf else -1)
