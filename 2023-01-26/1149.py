# 시간복잡도: O(N)
# 어려웠던 점: O(N)인걸 깨닫기까지 시간이 걸림

# 아이디어: 첫번째부터 마지막 집까지 R, G, B를 골랐을 때 각각 최소 비용을 기록
# 앞에 선택한 색상을 못 고를 뿐 사실상 그리디라고 생각해도 괜찮을 듯

from sys import stdin

input = stdin.readline
N = int(input())
dp = [[0] * (N + 1) for _ in range(3)]

for i in range(1, N + 1):
    cost = list(map(int, input().split()))
    for j in range(3):
        dp[j][i] += cost[j] + min(dp[j - 1][i - 1], dp[j - 2][i - 1])

print(min(dp[i][-1] for i in range(3)))
