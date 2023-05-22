t = int(input())

for _ in range(t):

    n, m = input().split()
    n, m = int(n), int(m)

    num_connected = [0 for _ in range(n+1)]

    for _ in range(m):
        u, v = input().split()
        u, v = int(u), int(v)
        num_connected[u] += 1
        num_connected[v] += 1

    freq = {}

    for i in num_connected[1:]:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1

    r, b = -1, -1

    for i in freq.keys():
        if freq[i] == 1:
            r = i
        elif freq[i] != 1 and i != 1:
            b = i

    if r == -1:
        print(b, b-1)
    else:
        print(r, b-1)