t = int(input())

for _ in range(t):

    n = int(input())
    arr = input().split()
    arr = [int(i) for i in arr]

    if n == 2:
        if arr[0] <= arr[1]:
            print('YES')
        else:
            print('NO')
        continue

    # forward pass
    for i in range(1, n-1):
        diff = arr[i-1] - arr[i]
        arr[i] += diff
        arr[i+1] += diff
    
    # backward pass
    for i in range(n-2, 0, -1):
        diff = arr[i] - arr[i+1]
        arr[i] -= diff
        arr[i-1] -= diff

    # final check
    if arr[0] <= arr[1]:
        print('YES')
    else:
        print('NO')
