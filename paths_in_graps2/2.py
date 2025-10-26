n, m = map(int, input().split())
edges = [[int(i) for i in input().split()] for _ in range(m)]
adj = [[] for _ in range(n + 1)]
for e in edges:
    adj[e[0]].append((e[1], e[2]))

inf = 10**9
dist = [inf] * (n + 1)
dist[1] = 0
for _ in range(m-1):
    flag = True
    for (u, v, cost) in edges:
        if dist[v] > dist[u] + cost:
            dist[v] = dist[u] + cost
            flag = False
    if flag:  # there is no improvement in the graph
        break


# Check if we still can improve some dist
# print(int(
#     any([dist[v] > dist[u] + cost for (u, v, cost) in edges])
# ))
if flag:
    print(0)
else:
    for (u, v, cost) in edges:
        if dist[v] > dist[u] + cost:
            print(1)
            break
    else:
        print(0)
