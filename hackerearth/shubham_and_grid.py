class Edge:
    def __init__(self, u, v, capacity, current_flow, residual=False):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.current_flow = current_flow
        self.residual = residual

    def get_residual_flow(self):
        return self.capacity - self.current_flow

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_adge(self, u, v, residual=False):
        capacity = 1
        if residual:
            capacity = 0

        if u in self.adj_list:
            self.adj_list[u][v] = Edge(u, v, capacity, 0, residual=residual)
        else:
            self.adj_list[u] = {v : Edge(u, v, capacity, 0, residual=residual)}

def dfs(graph, s, t, visited=set()):

    if s == t:
        return 1
    
    visited.add(s)
    
    for v in graph.adj_list[s]:
        if v in visited:
            continue
        edge = graph.adj_list[s][v]
        residual_edge = graph.adj_list[v][s]
        if edge.get_residual_flow() > 0:
            if dfs(graph, v, t, visited) == 1:
                edge.current_flow += 1
                residual_edge.current_flow -= 1
                return 1

    visited.remove(s)
    return 0

import pprint

graph = Graph()

n, m = input().split()
n, m = int(n), int(m)
grid = []
for _ in range(n):
    grid.append(input().split(" "))

# go through all points and add edges to 4-directional neighbors
for i in range(n):
    for j in range(m):
        u = grid[i][j]
        if u == 'a':
            graph.add_adge('s', (u, i, j))
            graph.add_adge((u, i, j), 's')
        if u == 'd':
            graph.add_adge((u, i, j), 't')
            graph.add_adge('t', (u, i, j))

        if i > 0 and grid[i-1][j] == chr(ord(u)+1):
            graph.add_adge((u, i, j), (grid[i-1][j], i-1, j), residual=False)
            graph.add_adge((grid[i-1][j], i-1, j), (u, i, j), residual=True)
        if j > 0 and grid[i][j-1] == chr(ord(u)+1):
            graph.add_adge((u, i, j), (grid[i][j-1], i, j-1), residual=False)
            graph.add_adge((grid[i][j-1], i, j-1), (u, i, j), residual=True)
        if i < n-1 and grid[i+1][j] == chr(ord(u)+1):
            graph.add_adge((u, i, j), (grid[i+1][j], i+1, j), residual=False)
            graph.add_adge((grid[i+1][j], i+1, j), (u, i, j), residual=True)
        if j < m-1 and grid[i][j+1] == chr(ord(u)+1):
            graph.add_adge((u, i, j), (grid[i][j+1], i, j+1), residual=False)
            graph.add_adge((grid[i][j+1], i, j+1), (u, i, j), residual=True)

# pprint.pprint(graph.adj_list)

# run dfs until you can't reach the target
max_flow = 0
while True:
    flow = dfs(graph, 's', 't', visited=set())
    if flow == 0:
        break
    max_flow += flow
    
print(max_flow)
