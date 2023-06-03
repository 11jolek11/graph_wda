from collections import deque

def bfs(graph, residual_capacity, source, sink, parent):
    visited = [False] * len(graph)
    queue = deque()
    queue.append(source)
    visited[source] = True

    while queue:
        u = queue.popleft()
        for v in range(len(graph)):
            if not visited[v] and residual_capacity[u][v] > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                if v == sink:
                    return True

    return False

def edmonds_karp(graph, source, sink):
    num_vertices = len(graph)
    residual_capacity = [[0] * num_vertices for _ in range(num_vertices)]

    for u in range(num_vertices):
        for v, capacity in graph[u].items():
            residual_capacity[u][v] = capacity

    max_flow = 0
    parent = [-1] * num_vertices

    while bfs(graph, residual_capacity, source, sink, parent):
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, residual_capacity[parent[s]][s])
            s = parent[s]

        max_flow += path_flow

        v = sink
        while v != source:
            u = parent[v]
            residual_capacity[u][v] -= path_flow
            residual_capacity[v][u] += path_flow
            v = parent[v]

    return max_flow


if __name__ == "__main__":
    graph = [
        {1: 10, 2: 10},  # edges from source (node 0)
        {3: 4, 4: 8},    # edges from node 1
        {4: 9, 5: 10},   # edges from node 2
        {5: 10},         # edges from node 3
        {6: 10},         # edges from node 4
        {6: 10},         # edges from node 5
        {}               # edges from sink (node 6)
    ]

    source = 0
    sink = 6

    max_flow = edmonds_karp(graph, source, sink)
    print("Maximum flow:", max_flow)
