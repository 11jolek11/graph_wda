from collections import defaultdict

def topological_sort(graph):
    # Create a dictionary to store the in-degree of each node
    in_degree = defaultdict(int)

    # Calculate the in-degree of each node
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    # Create a queue and enqueue all nodes with in-degree 0
    queue = []
    for node in graph:
        if in_degree[node] == 0:
            queue.append(node)

    # Initialize a list to store the sorted order
    sorted_order = []

    # Process each node in the queue
    while queue:
        node = queue.pop(0)
        sorted_order.append(node)

        # Reduce the in-degree of each neighbor of the current node
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1

            # If the in-degree of a neighbor becomes 0, enqueue it
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If there are still nodes remaining with in-degree > 0, there is a cycle in the graph
    if len(sorted_order) != len(graph):
        raise ValueError("The graph contains a cycle.")

    return sorted_order


if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D', 'E'],
        'D': ['E'],
        'E': []
    }

    try:
        sorted_order = topological_sort(graph)
        print("Topological sort order:", sorted_order)
    except ValueError as e:
        print("Error:", str(e))
