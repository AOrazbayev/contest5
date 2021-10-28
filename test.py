N = int(input())
n = input().split()
a = []
b = []
s = ""

print(n)

for c in n:
    print(c, end=' ')
    if c.isdigit():
        a.append(int(c))

print(a)

for i in range(1, N-1):
    if a[i] > a[i+1] and a[i] > a[i-1]:
        b.append(i)
        print("max", a[i])
    elif a[i] < a[i+1] and a[i] < a[i-1]:
        b.append(i)
        print("min", a[i])

for m in b:
    s += str(m) + " "

print(s)