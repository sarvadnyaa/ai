#4 Kruskal's Algorithm
#By sorting edges

def find(parent, i):
  while parent[i] != i:
    i = parent[i]
  return i

def kruskals(V, edges):
  edges.sort(key=lambda x: x[2])
  parent = list(range(V))
  total_cost = 0

  print("Edges \tWeight")

  for u, v, w in edges:
    root_u = find(parent, u)
    root_v = find(parent, v)

    if root_u != root_v:
      print(f"{u} - {v}\t{w}")
      total_cost += w
      parent[root_v] = root_u

  print("Total Cost:", total_cost)

edges = [
    (0, 1, 2),
    (1, 2, 3),
    (0, 3, 6),
    (1, 4, 5),
    (2, 4, 7)
]

kruskals(5, edges)
