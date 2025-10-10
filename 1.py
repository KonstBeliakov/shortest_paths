import heapq

IN = 'in'
OUT = 'out'

n, m = map(int, input().split())

# each edge is 3 numbers: from, to, and length
edges = [[int(i) for i in input().split()] for _ in range(m)]
graph = [{IN: [], OUT: []} for i in range(n + 1)]

for edge in edges:
    node1, node2, length = edge

    graph[node1][OUT].append((node2, length))
    graph[node2][IN].append((node1, length))


def bidirectional_djikstra(graph, node1: int, node2: int):
    if node1 == node2:
        return 0

    distances1 = [float('infinity') for _ in range(len(graph) + 1)]
    distances1[node1] = 0

    distances2 = [float('infinity') for _ in range(len(graph) + 1)]
    distances2[node2] = 0

    queue1 = [(0, node1)]
    queue2 = [(0, node2)]

    min_dist = float('infinity')

    while queue1 or queue2:
        if queue1 and (not queue2 or queue1[0][0] < queue2[0][0]):
            current_distance, current_vertex = heapq.heappop(queue1)
            if current_distance > distances1[current_vertex]:
                continue

            # ??
            if current_distance > min_dist:
                return min_dist

            for neigbor, weight in graph[current_vertex][OUT]:
                distance = current_distance + weight

                if distance < distances1[neigbor]:
                    distances1[neigbor] = distance
                    heapq.heappush(queue1, (distance, neigbor))
                    if distances2[neigbor] != float('infinity'):
                        min_dist = min(min_dist, distances1[neigbor] + distances2[neigbor])
        else:
            current_distance, current_vertex = heapq.heappop(queue2)
            if current_distance > distances2[current_vertex]:
                continue

            # ??
            if current_distance > min_dist:
                return min_dist

            for neigbor, weight in graph[current_vertex][IN]:
                distance = current_distance + weight

                if distance < distances2[neigbor]:
                    distances2[neigbor] = distance
                    heapq.heappush(queue2, (distance, neigbor))
                    if distances1[neigbor] != float('infinity'):
                        min_dist = min(min_dist, distances1[neigbor] + distances2[neigbor])

    return min_dist if min_dist != float('infinity') else -1


q = int(input())
for _ in range(q):
    u, v = map(int, input().split())
    print(bidirectional_djikstra(graph, u, v))
