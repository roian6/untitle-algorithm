N = int(input())
li = list(map(int, input().split()))
li2 = li[::-1]

dp = [[1] * N for _ in range(2)]
for i in range(N):
    for j in range(i):
        if li[j] < li[i]:
            dp[0][i] = max(dp[0][i], dp[0][j] + 1)
        if li2[j] < li2[i]:
            dp[1][i] = max(dp[1][i], dp[1][j] + 1)

ans = 0
for i in range(N):
    ans = max(ans, dp[0][i] + dp[1][N - i - 1] - 1)
print(ans)
