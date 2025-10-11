import heapq
import sys

IN = 1
OUT = 0

INF = 10**18


n, m = map(int, sys.stdin.readline().split())

# each edge is 3 numbers: from, to, and length
edges = [[int(i) for i in sys.stdin.readline().split()] for _ in range(m)]
graph = [[[], []] for i in range(n + 1)]

for edge in edges:
    node1, node2, length = edge

    graph[node1][OUT].append((node2, length))
    graph[node2][IN].append((node1, length))


distances = [[INF for _ in range(len(graph) + 1)] for _ in range(2)]
visited_nodes = [[], []]


def bidirectional_djikstra(graph, node1: int, node2: int):
    global visited_nodes, distances
    if node1 == node2:
        return 0

    for node in visited_nodes[OUT]:
        distances[OUT][node] = INF
    for node in visited_nodes[IN]:
        distances[IN][node] = INF
    visited_nodes = [[node1], [node2]]

    distances[OUT][node1] = 0
    distances[IN][node2] = 0

    queue = [[(0, node1)], [(0, node2)]]

    min_dist = INF

    while queue[IN] or queue[OUT]:
        if queue[OUT] and (not queue[IN] or queue[OUT][0][0] < queue[IN][0][0]):
            current_distance, current_vertex = heapq.heappop(queue[OUT])
            direction = OUT
        else:
            current_distance, current_vertex = heapq.heappop(queue[IN])
            direction = IN

        if current_distance > min_dist:
            return min_dist

        if current_distance > distances[direction][current_vertex]:
            continue

        for neigbor, weight in graph[current_vertex][direction]:
            distance = current_distance + weight

            if distance < distances[direction][neigbor]:
                distances[direction][neigbor] = distance
                heapq.heappush(queue[direction], (distance, neigbor))
                visited_nodes[direction].append(neigbor)
                if distances[(direction + 1) % 2][neigbor] != INF:
                    min_dist = min(min_dist, distances[IN][neigbor] + distances[OUT][neigbor])

    return min_dist if min_dist != INF else -1


q = int(input())
for _ in range(q):
    u, v = map(int, sys.stdin.readline().split())
    print(bidirectional_djikstra(graph, u, v))
