def pascal(n):
    r = [1]
    for _ in range(n+1):
        print(r)
        k = len(r)
        z = []
        for i in range(k-1):
            z.append(r[i] + r[i+1])
        r = [1] + z + [1]


n = int(input())
pascal(n)
