n, m = map(int, input().split())
edges = [[int(i) for i in input().split()] for _ in range(m)]

adj = [[] for _ in range(n + 1)]
adj_r = [[] for _ in range(n + 1)]

for edge in edges:
    adj[edge[0]].append(edge[1])
    adj_r[edge[1]].append(edge[0])

postorder = [None] * (n + 1)
current_postorder = 0
visited = [False] * (n + 1)
visited_order = []


def dfs(graph, vertex):
    global visited_order
    for v in graph[vertex]:
        if not visited[v]:
            visited[v] = True
            dfs(graph, v)
    visited_order.append(vertex)


for v in range(1, n + 1):
    if not adj_r[v]:  # there is no incoming edges in the original graph
        dfs(adj, v)

print(*reversed(visited_order))
