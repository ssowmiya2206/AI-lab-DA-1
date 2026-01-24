from collections import defaultdict, deque

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)
    order = []

    while queue:
        vertex = queue.popleft()
        order.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

# Example Usage
graph = {
    'Build': ['Test', 'Lint'],
    'Test': ['Package'],
    'Lint': ['Package'],
    'Package': ['Deploy'],
    'Deploy': []
}
print("BFS Order:", bfs(graph, 'Build'))
# Expected Output: BFS Order: ['Build', 'Test', 'Lint', 'Package', 'Deploy']
