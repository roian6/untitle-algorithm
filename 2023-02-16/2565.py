from sys import stdin

input = stdin.readline
N = int(input())
li = [tuple(map(int, input().split())) for _ in range(N)]
li.sort()

dp = [1] * N
for i in range(N):
    for j in range(i):
        if li[i][1] > li[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))
