
n, m = input().split()
n, m = int(n), int(m)

adj_list = {i: {} for i in range(1, n+1)}

for i in range(m):
    u, v, w = input().split()
    u, v, w = int(u), int(v), int(w)
    adj_list[u][v] = w

distances = [float('inf') for _ in range(n+1)]

from heapq import heappush, heappop

q = [(0, 1)]

while q:
    d, u = heappop(q)
    if distances[u] != float('inf'):
        continue
    distances[u] = d
    for v in adj_list[u].keys():
        w = adj_list[u][v]
        heappush(q, (d+w, v))

for i in range(2, n+1):
    if distances[i] == float('inf'):
        distances[i] = -1
    print(distances[i], end=" ")

print()