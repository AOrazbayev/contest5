n = int(input())
s = list(map(int, input().split()))
#print(s)

global_max = 0
local_max = 0

for i in range(n):
    if s[i] == 1:
        local_max = n
        for j in range(n):
            if s[j] == 2:
                local_max = min(abs(i-j), local_max)
    global_max = max(global_max, local_max)
print(global_max)