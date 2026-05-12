#1 DFS

def dfs(graph, start, visited=None):
  if visited is None:
    visited = set()

  print(start, end=" ")
  visited.add(start)

  for neighbour in graph[start]:
    if neighbour not in visited:
      dfs(graph, neighbour, visited)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

print("DFS Traversal:", end=" ")
dfs(graph, 'A')
