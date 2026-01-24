def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example Usage
graph = {
    'Build': ['Test', 'Lint'],
    'Test': ['Package'],
    'Lint': ['Package'],
    'Package': ['Deploy'],
    'Deploy': []
}
print("DFS Order:", end=" ")
dfs(graph, 'Build')
# Expected Output: DFS Order: Build Test Package Deploy Lint
