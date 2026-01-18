import heapq

def astar(graph, heuristic, start, goal):
    pq = [(heuristic[start], 0, start)]
    visited = {}

    while pq:
        f, g, node = heapq.heappop(pq)

        if node == goal:
            return g

        if node in visited and visited[node] <= g:
            continue

        visited[node] = g

        for neighbor, weight in graph[node]:
            new_g = g + weight
            new_f = new_g + heuristic[neighbor]
            heapq.heappush(pq, (new_f, new_g, neighbor))

    return None

graph = {}
heuristic = {}

n = int(input("Enter number of nodes: "))
for _ in range(n):
    node = input("Enter node: ")
    graph[node] = []
    heuristic[node] = int(input(f"Enter heuristic value for {node}: "))

e = int(input("Enter number of edges: "))
for _ in range(e):
    u, v, w = input("Enter edge (u v weight): ").split()
    graph[u].append((v, int(w)))

start = input("Enter start node: ")
goal = input("Enter goal node: ")

print("Minimum cost using A*:", astar(graph, heuristic, start, goal))
