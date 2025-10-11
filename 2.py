import heapq
import math

OUT = 0
IN = 1

n, m = map(int, input().split())

cords = [[0, 0]] + [[int(i) for i in input().split()] for _ in range(n)]

# from, to, length
edges = [[int(i) for i in input().split()] for _ in range(m)]

graph = [[[], []] for i in range(n + 1)]

for edge in edges:
    v, u, length = edge

    graph[v][OUT].append((u, length))
    graph[u][IN].append((v, length))


def A_star(graph, node1, node2):
    if node1 == node2:
        return 0

    distances = [[float('infinity') for _ in range(len(graph) + 1)] for _ in range(2)]
    distances[OUT][node1] = 0
    distances[IN][node2] = 0

    queue = [[(0, node1)], [(0, node2)]]

    min_dist = float('infinity')

    while queue[IN] or queue[OUT]:
        if queue[OUT] and (not queue[IN] or queue[OUT][0][0] < queue[IN][0][0]):
            current_distance, current_vertex = heapq.heappop(queue[OUT])
            direction = OUT
            goal = node2
        else:
            current_distance, current_vertex = heapq.heappop(queue[IN])
            direction = IN
            goal = node1

        if current_distance > distances[direction][current_vertex]:
            continue

        dist = math.hypot(cords[current_vertex][0] - cords[goal][0], cords[current_vertex][1] - cords[goal][1])
        if current_distance + dist > min_dist:
            return min_dist

        for neigbor, weight in graph[current_vertex][direction]:
            distance = current_distance + weight

            if distance < distances[direction][neigbor]:
                distances[direction][neigbor] = distance
                heapq.heappush(queue[direction], (distance, neigbor))
                if distances[(direction + 1) % 2][neigbor] != float('infinity'):
                    min_dist = min(min_dist, distances[IN][neigbor] + distances[OUT][neigbor])

    return min_dist if min_dist != float('infinity') else -1


q = int(input())
for _ in range(q):
    u, v = map(int, input().split())
    print(A_star(graph, u, v))
