import sys
import queue
import math


class AStar:
    def __init__(self, n, adj, cost, x, y):
        self.n = n
        self.adj = adj
        self.cost = cost
        self.inf = n * 10 ** 6
        self.d = [self.inf] * n
        self.visited = [False] * n
        self.workset = []
        self.x = x
        self.y = y

    def clear(self):
        for v in self.workset:
            self.d[v] = self.inf
            self.visited[v] = False
        del self.workset[0:len(self.workset)]

    def heuristic(self, u, t):
        dx = self.x[u] - self.x[t]
        dy = self.y[u] - self.y[t]
        return math.sqrt(dx * dx + dy * dy)

    def visit(self, q, p, v, dist, measure):
        if self.d[v] > dist:
            self.d[v] = dist
            self.visited[v] = True
            self.workset.append(v)
            q.put((dist + measure, v))

    def query(self, s, t):
        self.clear()
        q = queue.PriorityQueue()
        self.d[s] = 0
        self.visited[s] = True
        self.workset.append(s)

        q.put((self.heuristic(s, t), s))

        while not q.empty():
            _, u = q.get()

            if u == t:
                return self.d[t]

            if self.visited[u]:
                for i in range(len(self.adj[u])):
                    vertex = self.adj[u][i]
                    cost = self.cost[u][i]
                    new_dist = self.d[u] + cost

                    if self.d[vertex] > new_dist:
                        self.visit(q, u, vertex, new_dist, self.heuristic(vertex, t))

                self.visited[u] = False

        return -1


def readl():
    return map(int, sys.stdin.readline().split())


if __name__ == '__main__':
    n, m = readl()
    x = [0 for _ in range(n)]
    y = [0 for _ in range(n)]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]

    for i in range(n):
        a, b = readl()
        x[i] = a
        y[i] = b

    for e in range(m):
        u, v, c = readl()
        adj[u - 1].append(v - 1)
        cost[u - 1].append(c)

    t, = readl()
    astar = AStar(n, adj, cost, x, y)

    for i in range(t):
        s, t = readl()
        print(astar.query(s - 1, t - 1))
