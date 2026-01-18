def dfs(graph, start):
    visited = set()
    stack = [start]

    print("DFS Traversal:", end=" ")

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in reversed(graph[node]):
                stack.append(neighbor)


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
dfs(graph, start)
