# 시간복잡도: O(N^2)
# 어려웠던 점: LIS를 알면 응용하기 쉬움

# 아이디어: 현재 숫자보다 작은 숫자가 가진 가장 큰 증가 부분 수열의 합에 현재 숫자를 더한 값을 dp에 기록

N = int(input())
li = list(map(int, input().split()))
dp = [0] * N

ans = 0
for i in range(N):
    dp[i] = li[i]
    for j in range(i):
        if li[i] > li[j] and dp[j] + li[i] > dp[i]:
            dp[i] = dp[j] + li[i]
    ans = max(ans, dp[i])

print(ans)
