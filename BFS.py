graph = {
    '5' : ['3','7'],
    '3' : ['2', '4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}

visited = []
q = []

def bfs(visited, graph, node):
    visited.append(node)
    q.append(node)

    while q:
      m = q.pop(0)
      print(m, end = " ")

      for neighbour in graph[m]:
        if neighbour not in visited:
            visited.append(neighbour)
            q.append(neighbour)

print("BFS: ")
bfs(visited, graph, '5')