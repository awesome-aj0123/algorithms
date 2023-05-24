
"""
Finding minimum distance between vertex 1 and n
"""

import heapq

n, m = input().split()
n = int(n)
m = int(m)
nodes = n

adj_list = {i: {} for i in range(1, n+1)}

parents = [-1 for _ in range(n+1)]
visited = set()

for _ in range(m):
    a, b, w = input().split()
    a = int(a)
    b = int(b)
    w = int(w)
    adj_list[a][b] = w
    adj_list[b][a] = w 

q = [(0, 1, -1)]

while q:
    d, n, p = heapq.heappop(q)
    if n in visited:
        continue
    visited.add(n)
    parents[n] = p
    # check all the edges of n
    for to in adj_list[n].keys():
        if to in visited: # because we can have cycles
            continue
        w = adj_list[n][to]
        heapq.heappush(q, (d+w, to, n))

rev_res = []
i = nodes
while i != -1:
    rev_res.append(i)
    i = parents[i]
    
if rev_res[-1] != 1:
    print(-1)
else:
    for i in range(len(rev_res)-1, -1, -1):
        print(rev_res[i], end=" ")
    print()