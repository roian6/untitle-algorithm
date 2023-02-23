N = int(input())
li = list(map(int, input().split()))
d = {li[0]: 1}
for i in range(N):
    n = 1
    for j in range(i):
        if li[i] > li[j]:
            n = max(n, d[li[j]] + 1)
    d[li[i]] = n

print(max(d.values()))
