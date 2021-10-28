n, cycle_size = map(int, input().split())
arr = []
for i in range(1, n+1):
    arr.append(i)
print(arr)
kick = 0
start = 0
for j in range(n-1):
    start = kick % len(arr)
    kick = (start + cycle_size - 1) % len(arr)
    arr.pop(kick)
print(arr[0])
