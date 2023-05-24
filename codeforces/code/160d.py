class UnionFind:
    def __init__(self, nodes):
        self.parents = nodes
        self.rank = [0 for _ in range(len(nodes))]

    def root(self, i):
        while self.parents[i] != i:
            i = self.parents[i]
        return i
    
    def same(self, i, j):
        return self.root(i) == self.root(j)
    
    def union(self, i, j):
        a = self.root(i)
        b = self.root(j)
        if self.rank[a] < self.rank[b]:
            self.parents[a] = b
        elif self.rank[b] < self.rank[a]:
            self.parents[b] = a
        else:
            self.parents[a] = b
            self.rank[b] += 1


n, m = input().split()
n, m = int(n), int(m)

dsu = UnionFind(nodes=[i for i in range(n+1)])

edge_freq = {i: {} for i in range(1, n+1)}

edges_og = []

for _ in range(m):
    u, v, w = input().split()
    u, v, w = int(u), int(v), int(w)

    edge_freq[u][w] = edge_freq[u].get(w, 0) + 1
    edge_freq[v][w] = edge_freq[v].get(w, 0) + 1

    edges_og.append((w, u, v))

edges = edges_og[:]
edges.sort()

res = {}

for w, u, v in edges:
    # check both u and v nodes to see if there are any duplicate weights
    if edge_freq[u][w] == 1 and edge_freq[v][w] == 1 and not dsu.same(u, v):
        dsu.union(u, v)
        res[(u, v)] = "any"
    elif edge_freq[u][w] > 1 or edge_freq[v][w] > 1 and not dsu.same(u, v):
        dsu.union(u, v)
        res[(u, v)] = "at least one"
    else:
        res[(u, v)] = "none"

for w, u, v in edges_og:
    print(res[(u, v)])