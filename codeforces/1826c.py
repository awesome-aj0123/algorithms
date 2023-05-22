
N = int(1e6 + 10)
min_div = [0 for _ in range(N)]
# proeprocessing
d = 2
while d*d < N:
    if min_div[d] == 0:
        min_div[d] = d
        for i in range(d*d, N, d):
            if min_div[i] == 0:
                min_div[i] = d
    d += 1

# for all prime numbers greater than sqrt(N)
for i in range(1, N):
    if min_div[i] == 0:
        min_div[i] = i

t = int(input())

for _ in range(t):

    a, b = input().split()
    a, b = int(a), int(b)

    # print(a, b, min_div[a])

    if a == 1 or min_div[a] > b:
        print('YES')
    else:
        print('NO')
        