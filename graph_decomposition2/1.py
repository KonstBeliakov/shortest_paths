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


def dfs_postorder_count(graph, vertex):
    # print(f'dfs_postorder_count, {vertex=}')
    global postorder, current_postorder, visited_order
    for v in graph[vertex]:
        if not visited[v]:
            visited[v] = True
            dfs_postorder_count(graph, v)
    postorder[vertex] = current_postorder
    current_postorder += 1
    visited_order.append(vertex)


def dfs_cycle_search(graph, vertex):
    global reachable
    reachable[vertex] = True
    # print(f'dfs_cycle_search{vertex=}')
    for v in graph[vertex]:
        if not reachable[v]:
            if dfs_cycle_search(graph, v):
                return 1
        else:
            return 1
    return 0


reachable = [False] * (n+1)
dfs_postorder_count(adj_r, 1)
print(dfs_cycle_search(adj, visited_order[-1]))
