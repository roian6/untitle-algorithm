# 시간복잡도: O(N)
# 어려웠던 점: 배낭 문제인걸 모르면 헤멜 수 있음

from sys import stdin

input = stdin.readline
T = int(input())
for _ in range(T):
    N, li, M = int(input()), list(map(int, input().split())), int(input())

    dp = [1] + [0] * M
    for n in li:
        for j in range(n, M + 1):
            dp[j] += dp[j - n]

    print(dp[M])
