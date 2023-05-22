
t = int(input())

for _ in range(t):

    n = int(input())
    graph = {i: set() for i in range(1, n+1)}

    visited = {i: False for i in range(1, n+1)}

    for i in range(n):
        line = input()
        for j in range(len(line)):
            if line[j] == "1":
                graph[i+1].add(j+1)


    topological_order = []

    # get topoliogical order
    def postorder(node):
        visited[node] = True

        if len(graph[node]) == 0:
            topological_order.insert(0, node)
            return
        
        for next_node in graph[node]:
            if not visited[next_node]:
                postorder(next_node)

        topological_order.insert(0, node)
        return

    for i in range(1, n+1):
        if not visited[i]:
            postorder(i)

    sets = [set() for _ in range(n+1)]
    v = 1
    for i in topological_order:  
        sets[i].add(v)
        for j in graph[i]:
            sets[j] = sets[j].union(sets[i])
        v += 1

    for i in range(1, n+1):
        print(len(sets[i]), end=" ")
        l = list(sets[i])
        for j in l:
            print(j, end=" ")
        
        print()