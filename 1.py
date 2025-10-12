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


def bidirectional_djikstra(graph, node1: int, node2: int):
    if node1 == node2:
        return 0

    visited_nodes = [{node1: 0}, {node2: 0}]

    queue = [[(0, node1)], [(0, node2)]]

    min_dist = INF

    while queue[IN] and queue[OUT]:
        if queue[OUT][0] < queue[IN][0]:
            current_distance, current_vertex = heapq.heappop(queue[OUT])
            direction = OUT
        else:
            current_distance, current_vertex = heapq.heappop(queue[IN])
            direction = IN

        if current_distance * 2 > min_dist:
            return min_dist

        if current_distance > visited_nodes[direction].get(current_vertex, INF):
            continue

        for neighbor, weight in graph[current_vertex][direction]:
            distance = current_distance + weight

            if distance < visited_nodes[direction].get(neighbor, INF):
                visited_nodes[direction][neighbor] = distance
                heapq.heappush(queue[direction], (distance, neighbor))
                if neighbor in visited_nodes[(direction + 1) % 2]:
                    min_dist = min(min_dist, visited_nodes[IN][neighbor] + visited_nodes[OUT][neighbor])

    return min_dist if min_dist != INF else -1


q = int(input())
for _ in range(q):
    u, v = map(int, sys.stdin.readline().split())
    print(bidirectional_djikstra(graph, u, v))
