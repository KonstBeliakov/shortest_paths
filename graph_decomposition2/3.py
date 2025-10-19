# SCCs(G)
# Run DFS(G^R)
# for v in V in reverse postorder:
# 	if not visited(v):
# 		Explore(v)
# 		mark visited vertices as nwe SCC

import sys
sys.setrecursionlimit(10 ** 6)


n, m = map(int, input().split())
edges = [[int(i) for i in input().split()] for _ in range(m)]
adj = [[] for _ in range(n + 1)]
adj_r = [[] for _ in range(n + 1)]
for edge in edges:
    adj[edge[0]].append(edge[1])
    adj_r[edge[1]].append(edge[0])

adj_r_visited = [False] * (n + 1)
visit_order = []


def dfs_postorder(adj, vertex):
    global visit_order
    adj_r_visited[vertex] = True
    for v in adj[vertex]:
        if not adj_r_visited[v]:
            dfs_postorder(adj, v)
    visit_order.append(vertex)


def dfs_mark_components(adj, vertex):
    global visited, current_component_number
    for v in adj[vertex]:
        if component[v] is None:
            component[v] = current_component_number
            dfs_mark_components(adj, v)


for v in range(1, n + 1):
    if not adj_r_visited[v]:
        dfs_postorder(adj_r, v)

component = [None] * (n + 1)
current_component_number = 0
for v in reversed(visit_order):
    if component[v] is None:
        current_component_number += 1
        dfs_mark_components(adj, v)
print(current_component_number)
