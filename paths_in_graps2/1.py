import heapq
n, m = map(int, input().split())
edges = [[int(i) for i in input().split()] for _ in range(m)]  # node1, node2, cost
adj = [[] for _ in range(n + 1)]
for e in edges:
    adj[e[0]].append((e[1], e[2]))
u, v = map(int, input().split())

q = [(0, u)]
visited = [False] * (n + 1)
inf = 10**9
dist = [inf] * (n + 1)
while q:
    node_cost, node = heapq.heappop(q)
    dist[node] = min(dist[node], node_cost)
    if not visited[node]:
        for (neighbor, cost) in adj[node]:
            heapq.heappush(q, (node_cost + cost, neighbor))
        visited[node] = True
print(dist[v])
