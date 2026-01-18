import heapq

def ucs(graph, start, goal):
    pq = [(0, start)]
    visited = set()

    while pq:
        cost, node = heapq.heappop(pq)

        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            return cost

        for neighbor, weight in graph[node]:
            heapq.heappush(pq, (cost + weight, neighbor))

    return None

graph = {}
n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("Enter node: ")
    graph[node] = []

e = int(input("Enter number of edges: "))
for _ in range(e):
    u, v, w = input("Enter edge (u v weight): ").split()
    graph[u].append((v, int(w)))

start = input("Enter start node: ")
goal = input("Enter goal node: ")

result = ucs(graph, start, goal)
print("Minimum cost:", result)
