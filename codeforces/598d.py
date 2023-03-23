"""
ACTUAL SOLNL
Find open square, do DFS to calculate number of blocks
Do DFS again to populate surrounding open squares with same value
Do for all groups of open squares
"""


n, m, k = input().split()
n, m, k = int(n), int(m), int(k)

def is_valid(i, j):
    return 0 <= i and i < n and 0 <= j and j < m

grid = []
for _ in range(n):
    row = list(input())
    grid.append(row)


def recurse(i, j, visited):
    # print(visited[i][j])
    # print(grid[i][j] == '*')
    # print(not is_valid(i, j))
    if visited[i][j] or grid[i][j] == '*' or not is_valid(i, j):
        return 0
    
    paintings = 0
    if is_valid(i-1, j) and grid[i-1][j] == "*":
        paintings += 1
    if is_valid(i+1, j) and grid[i+1][j] == "*":
        paintings += 1
    if is_valid(i, j-1) and grid[i][j-1] == "*":
        paintings += 1
    if is_valid(i, j+1) and grid[i][j+1] == "*":
        paintings += 1

    visited[i][j] = True

    paintings += recurse(i-1, j, visited)
    paintings += recurse(i+1, j, visited)
    paintings += recurse(i, j-1, visited)
    paintings += recurse(i, j+1, visited)

    return paintings

for _ in range(k):

    i, j = input().split()
    i, j = int(i), int(j)
    visited = [[False for _ in range(m)] for _ in range(n)]

    print(recurse(i-1, j-1, visited))

    

    