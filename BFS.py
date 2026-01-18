from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    print("BFS Traversal:", end=" ")

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in graph[node]:
                queue.append(neighbor)


graph = {}
n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("Enter node: ")
    graph[node] = []

e = int(input("Enter number of edges: "))
for _ in range(e):
    u, v = input("Enter edge (u v): ").split()
    graph[u].append(v)

start = input("Enter start node: ")
bfs(graph, start)
