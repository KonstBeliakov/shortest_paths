#include <bits/stdc++.h>
using namespace std;

const long long INF = 1e18;
const int IN = 1;
const int OUT = 0;

int n, m;
vector<pair<int, long long>> graph[100005][2];
long long distances[2][100005];
vector<int> visited_nodes[2];

long long bidirectional_dijkstra(int node1, int node2) {
    if (node1 == node2) {
        return 0;
    }

    // Reset distances for visited nodes
    for (int node : visited_nodes[OUT]) {
        distances[OUT][node] = INF;
    }
    for (int node : visited_nodes[IN]) {
        distances[IN][node] = INF;
    }
    visited_nodes[OUT].clear();
    visited_nodes[IN].clear();
    visited_nodes[OUT].push_back(node1);
    visited_nodes[IN].push_back(node2);

    distances[OUT][node1] = 0;
    distances[IN][node2] = 0;

    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> queue[2];
    queue[OUT].push({0, node1});
    queue[IN].push({0, node2});

    long long min_dist = INF;

    while (!queue[OUT].empty() || !queue[IN].empty()) {
        int direction;
        long long current_distance;
        int current_vertex;

        if (!queue[OUT].empty() && (queue[IN].empty() || queue[OUT].top().first < queue[IN].top().first)) {
            auto [d, v] = queue[OUT].top();
            queue[OUT].pop();
            current_distance = d;
            current_vertex = v;
            direction = OUT;
        } else {
            auto [d, v] = queue[IN].top();
            queue[IN].pop();
            current_distance = d;
            current_vertex = v;
            direction = IN;
        }

        if (current_distance > min_dist) {
            return min_dist;
        }

        if (current_distance > distances[direction][current_vertex]) {
            continue;
        }

        for (auto [neighbor, weight] : graph[current_vertex][direction]) {
            long long distance = current_distance + weight;

            if (distance < distances[direction][neighbor]) {
                distances[direction][neighbor] = distance;
                queue[direction].push({distance, neighbor});
                visited_nodes[direction].push_back(neighbor);

                if (distances[(direction + 1) % 2][neighbor] != INF) {
                    min_dist = min(min_dist, distances[IN][neighbor] + distances[OUT][neighbor]);
                }
            }
        }
    }

    return min_dist != INF ? min_dist : -1;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m;

    for (int i = 0; i < m; i++) {
        int node1, node2;
        long long length;
        cin >> node1 >> node2 >> length;

        graph[node1][OUT].push_back({node2, length});
        graph[node2][IN].push_back({node1, length});
    }

    int q;
    cin >> q;
    while (q--) {
        int u, v;
        cin >> u >> v;
        cout << bidirectional_dijkstra(u, v) << "\n";
    }

    return 0;
}