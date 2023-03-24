
class Edge:
    """
    Edge class to maintain each connect between two nodes and also the residual capacity (= original capacity - current flow)
    """
    def __init__(self, u, v, capacity, current_flow, residual):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.current_flow = current_flow
        self.residual = residual

class Graph:
    """
    Generic graph class
    """
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v, w, residual=False):
        if u in self.adj_list:
            self.adj_list[u][v] = Edge(u, v, w, 0, residual)
        else:
            self.adj_list[u] = {}
            self.adj_list[u][v] = Edge(u, v, w, 0, residual)

    def print_adj_list(self):
        import pprint
        pprint.pprint(self.adj_list)
        
def create_residual_graph(edges):
    """
    Creates the residual graph with the original and residual edges
    """
    
    # define the graph with regular edges and their residual counterparts
    graph = Graph()
    for edge in edges:
        u, v, w = edge
        graph.add_edge(u, v, w, residual=False)
        graph.add_edge(v, u, 0, residual=True)

    return graph

def dfs(graph, s, t, found_res, visited=set()):
    # runs the DFS algorithm to see if there is an augmented path from s to t

    if s == t:
        return True, float('inf')

    visited.add(s)
    
    for v in graph.adj_list[s].keys():
        if v in visited:
            continue
        residual_capacity = graph.adj_list[s][v].capacity - graph.adj_list[s][v].current_flow
        if residual_capacity > 0:
            found, max_flow = dfs(graph, v, t, found_res, visited)
            if found:
                found_res.append((s, v))
                return True, min(max_flow, residual_capacity)
    
    visited.remove(s)

    return False, -1
    

if __name__ == '__main__':

    # assuming n nodes
    # source = n - 1
    # target = n - 2

    file = "network.txt"
    with open(file, 'r+') as f:
        lines = f.readlines()
        edges = []
        for l in lines:
            l = l.strip().split(', ')
            edges.append((int(l[0]), int(l[1]), int(l[2])))

    # first create the graph with all the input and edges and their residual edges
    # we know that there can only be residual edges for input edges since we can't
    # ever flow directly from one node to another where there is no connection
    residual_graph = create_residual_graph(edges)

    # now we will begin runnning Ford-Fulkerson

    # get a path from s to t using dfs
    # then update the normal edges and the residual edges by the min residual capacity
    found = True
    total_flow = 0
    i = 0
    while True:
        print(f'running round {i+1} of dfs')
        found_res = []
        found, max_residual_flow = dfs(residual_graph, 5, 4, found_res, visited=set())
        if not found:
            break
        min_residual_capacity = min([residual_graph.adj_list[u][v].capacity - residual_graph.adj_list[u][v].current_flow for u, v in found_res])
        total_flow += min_residual_capacity
        for edge in found_res:
            u, v = edge
            residual_graph.adj_list[u][v].current_flow += min_residual_capacity
            residual_graph.adj_list[v][u].current_flow -= min_residual_capacity

        i += 1
    print('done.')
    print(f'max flow = {total_flow}')


