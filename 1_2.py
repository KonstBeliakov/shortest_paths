import heapq
import sys

input = sys.stdin.readline

IN, OUT = 1, 0
INF = 10**18

n, m = map(int, input().split())

graph = [[[] for _ in range(n + 1)], [[] for _ in range(n + 1)]]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[OUT][u].append((v, w))
    graph[IN][v].append((u, w))

dist = [[INF] * (n + 1) for _ in range(2)]
used = [0] * (n + 1)
timestamp = 0


def bidij(s, t):
    global timestamp
    timestamp += 1

    if s == t:
        return 0

    q = [[], []]
    dist[OUT][s] = 0
    dist[IN][t] = 0
    heapq.heappush(q[OUT], (0, s))
    heapq.heappush(q[IN], (0, t))

    min_dist = INF

    while q[OUT] or q[IN]:
        for side in (OUT, IN):
            if not q[side]:
                continue

            d, v = heapq.heappop(q[side])
            if d != dist[side][v]:
                continue

            if dist[OUT][v] + dist[IN][v] < min_dist:
                min_dist = dist[OUT][v] + dist[IN][v]

            for u, w in graph[side][v]:
                nd = d + w
                if nd < dist[side][u]:
                    dist[side][u] = nd
                    heapq.heappush(q[side], (nd, u))

        if q[OUT] and q[IN]:
            if q[OUT][0][0] + q[IN][0][0] >= min_dist:
                break

    return -1 if min_dist == INF else min_dist


q = int(input())
for _ in range(q):
    s, t = map(int, input().split())
    print(bidij(s, t))
