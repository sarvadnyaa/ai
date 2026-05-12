# Recursive BFS
from collections import deque

def bfs(graph, queue, visited):
    if not queue:
        return

    node = queue.popleft()

    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)

    bfs(graph, queue, visited)


# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

print("BFS Traversal:", end=" ")
bfs(graph, deque(['A']), set())
