n, m = map(int, input().split())
edges = [[int(i) for i in input().split()] for i in range(m)]

adj = [[] for _ in range(n + 1)]
for edge in edges:
    adj[edge[0]].append(edge[1])
    adj[edge[1]].append(edge[0])

visited = set()


def dfs(adj, start, end):
    if start == end:
        return 1

    global visited
    visited.add(start)
    for vertex in adj[start]:
        if vertex not in visited and dfs(adj, vertex, end):
            return 1
    return 0


u, v = map(int, input().split())
print(dfs(adj, u, v))
