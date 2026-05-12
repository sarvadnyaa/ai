#2 A-star

def astar(graph, heuristic, start, goal):
  open_list = [(0, start)]
  cost = {start:0}
  parent = {start:None}

  while open_list:
    open_list.sort()
    current_cost, current = open_list.pop(0)

    if current == goal:
      path = []
      while current:
        path.append(current)
        current = parent[current]
      return path[::-1]

    for neighbour, weight in graph[current]:
      new_cost = cost[current] + weight
      if neighbour not in cost or new_cost < cost[neighbour]:
        cost[neighbour] = new_cost
        priority = new_cost + heuristic[neighbour]
        open_list.append((priority, neighbour))
        parent[neighbour] = current

graph = {
    'A': [('B',1), ('C',3)],
    'B': [('D',1)],
    'C': [('D',1)],
    'D': []
}

heuristic = {'A':3, 'B':2, 'C':1, 'D':0}

print("A* path: ", astar(graph, heuristic, 'A', 'D'))
