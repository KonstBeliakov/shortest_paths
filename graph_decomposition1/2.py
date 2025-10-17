# Count the number of connected components
n, m = map(int, input().split())
edges = [[int(i) for i in input().split()] for i in range(m)]

adj = [[] for _ in range(n + 1)]
for edge in edges:
    adj[edge[0]].append(edge[1])
    adj[edge[1]].append(edge[0])

component = [None] * (n + 1)


def dfs(adj, start):
    global component, component_counter
    for vertex in adj[start]:
        if component[vertex] != component_counter:
            component[vertex] = component_counter
            dfs(adj, vertex)


component_counter = 0
for i in range(1, n + 1):
    if component[i] is None:
        component_counter += 1
        dfs(adj, i)
print(component_counter)
