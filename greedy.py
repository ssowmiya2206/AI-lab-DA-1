import heapq

def greedy(graph, heuristic, start, goal):
    pq = [(heuristic[start], start)]
    visited = set()

    while pq:
        _, node = heapq.heappop(pq)

        if node == goal:
            return True

        visited.add(node)
        for neighbor, _ in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic[neighbor], neighbor))

    return False

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

print("Goal Found:", greedy(graph, heuristic, start, goal))
