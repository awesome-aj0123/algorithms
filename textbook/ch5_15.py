class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_node(self, u):
        if u not in self.adj_list:
            self.adj_list[u] = set()

    def add_edge(self, u, v):
        self.adj_list[u].add(v)

def bfs(graph, s, t):
    q = []
    q.append((s, 0))
    while q:
        node, dist = q.pop(0)
        if node == t:
            return dist
        for v in graph.adj_list[node]:
            q.append((v, dist+1))

    return -1

import pprint

graph = Graph()

file = "ch5_15.txt"
with open(file, 'r+') as f:
    lines = f.readlines()
    for l in lines:
        u, v, c = l.strip().split(', ')

        u1r = u + '1r'
        u2r = u + '2r'
        u1b = u + '1b'
        u2b = u + '2b'

        v1r = v + '1r'
        v2r = v + '2r'
        v1b = v + '1b'
        v2b = v + '2b'

        graph.add_node(u1r)
        graph.add_node(u2r)
        graph.add_node(u1b)
        graph.add_node(u2b)
        graph.add_node(v1r)
        graph.add_node(v2r)
        graph.add_node(v1b)
        graph.add_node(v2b)

        if c == 'r':
            graph.add_edge(u1r, v2r)
            graph.add_edge(u1b, v1r)
            graph.add_edge(u2b, v1r)
        elif c == 'b':
            graph.add_edge(u1b, v2b)
            graph.add_edge(u1r, v1b)
            graph.add_edge(u2r, v1b)

graph.add_node('s')
graph.add_node('t')

graph.add_edge('s', 's1r')
graph.add_edge('s', 's1b')

graph.add_edge('t1r', 't')
graph.add_edge('t2r', 't')
graph.add_edge('t1b', 't')
graph.add_edge('t2b', 't')

# pprint.pprint(graph.adj_list)

res = bfs(graph, 's', 't') - 2
print(res)

    