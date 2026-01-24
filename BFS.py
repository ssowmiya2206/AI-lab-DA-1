from collections import deque

# Graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

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

def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()
    visited.add(start_node)
    
    # Process node
    for next_node in set(graph[start_node]) - visited:
        dfs(graph, next_node, visited)
    return visited

if __name__ == "__main__":
    print("BFS Order:", bfs(graph, 'A'))
    # DFS order can vary based on set subtraction order
    print("DFS Visited:", list(dfs(graph, 'A')))
