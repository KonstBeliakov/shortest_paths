# Check if graph is bipartite
n, m = map(int, input().split())
edges = [[int(i) for i in input().split()] for _ in range(m)]
adj = [[] for _ in range(n + 1)]
for e in edges:
    adj[e[0]].append(e[1])
    adj[e[1]].append(e[0])


def bfs(node):
    global dist, adj
    current_vertices = {node}

    dist[node] = 0
    while current_vertices:
        new_v = set()
        for node in current_vertices:
            for neigbor in adj[node]:
                if dist[neigbor] is None:
                    dist[neigbor] = dist[node] + 1
                    new_v.add(neigbor)
        current_vertices = new_v
    return dist


dist = [None] * (len(adj) + 1)
for i in range(n):
    if dist[i] is None:
        bfs(i)

# searching for adjacent vertices on the same distance level
print(int(all(
    [dist[e[0]] != dist[e[1]] for e in edges]
)))

