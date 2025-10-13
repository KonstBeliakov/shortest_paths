#!/usr/bin/python3
import sys
import queue


class BiDij:
    def __init__(self, n):
        self.n = n  # Number of nodes
        self.inf = n * 10 ** 6  # All distances in the graph are smaller
        self.d = [[self.inf] * n, [self.inf] * n]  # Initialize distances for forward and backward searches
        self.visited = [False] * n  # visited[v] == True iff v was visited by forward or backward search
        self.workset = []  # All the nodes visited by forward or backward search

    def clear(self):
        """Reinitialize the data structures for the next query after the previous query."""
        for v in self.workset:
            self.d[0][v] = self.d[1][v] = self.inf
            self.visited[v] = False
        del self.workset[0:len(self.workset)]

    def visit(self, q, side, v, dist):
        """Try to relax the distance to node v from direction side by value dist."""
        if dist < self.d[side][v]:
            self.d[side][v] = dist
            q[side].put((dist, v))
            if not self.visited[v]:
                self.visited[v] = True
                self.workset.append(v)

    def query(self, adj, cost, s, t):
        """Find shortest path from s to t using bidirectional Dijkstra."""
        self.clear()
        q = [queue.PriorityQueue(), queue.PriorityQueue()]
        self.visit(q, 0, s, 0)
        self.visit(q, 1, t, 0)

        ans = self.inf

        while not q[0].empty() or not q[1].empty():
            # Process from forward direction
            if not q[0].empty():
                d, u = q[0].get()
                if d > self.d[0][u]:
                    continue

                # Check if we found a meeting point
                if self.d[1][u] < self.inf:
                    ans = min(ans, self.d[0][u] + self.d[1][u])

                # Relax edges
                for i, v in enumerate(adj[0][u]):
                    self.visit(q, 0, v, d + cost[0][u][i])

            # Process from backward direction
            if not q[1].empty():
                d, u = q[1].get()
                if d > self.d[1][u]:
                    continue

                # Check if we found a meeting point
                if self.d[0][u] < self.inf:
                    ans = min(ans, self.d[0][u] + self.d[1][u])

                # Relax edges
                for i, v in enumerate(adj[1][u]):
                    self.visit(q, 1, v, d + cost[1][u][i])

        return ans if ans < self.inf else -1


def readl():
    return map(int, sys.stdin.readline().split())


if __name__ == '__main__':
    n, m = readl()
    adj = [[[] for _ in range(n)], [[] for _ in range(n)]]
    cost = [[[] for _ in range(n)], [[] for _ in range(n)]]
    for e in range(m):
        u, v, c = readl()
        adj[0][u - 1].append(v - 1)
        cost[0][u - 1].append(c)
        adj[1][v - 1].append(u - 1)
        cost[1][v - 1].append(c)
    t, = readl()
    bidij = BiDij(n)
    for i in range(t):
        s, t = readl()
        print(bidij.query(adj, cost, s - 1, t - 1))