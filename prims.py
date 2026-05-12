#3 Prim's Algorithm
#One vertex at a time

import sys

def prims(graph, V):
  selected = [False] * V
  selected[0] = True
  total_cost = 0

  print("Edge \tWeight")

  for _ in range(V-1):
    minimum = sys.maxsize
    x = y = 0

    for i in range(V):
      if selected[i]:
        for j in range(V):
          if not selected[j] and graph[i][j]:
            if minimum > graph[i][j]:
              minimun = graph[i][j]
              x, y = i, j


    print(f"{x} - {y}\t{graph[x][y]}")
    total_cost += graph[x][y]
    selected[y] = True

  print("Total Cost:", total_cost)

graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

prims(graph, 5)
