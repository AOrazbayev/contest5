# def cycle_shift(arr, N):
#     x = arr.pop(0)
#     arr.append(x)

def cycle_shift(arr, N):
    print(arr)
    print(arr[-1])
    t=arr[0]
    for i in range(0, N-1, 1):
        arr[i]=arr[i+1]
    arr[-1]=t


c = list(map(int, input().split()))

cycle_shift(c, 5)

print(c)