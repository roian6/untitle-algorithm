N = int(input())
li = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(N)]
dp[0][li[0]] = 1

for i in range(1, N - 1):
    for j in range(21):
        if j + li[i] <= 20:
            dp[i][j] += dp[i - 1][j + li[i]]
        if j - li[i] >= 0:
            dp[i][j] += dp[i - 1][j - li[i]]

print(dp[N - 2][li[N - 1]])
