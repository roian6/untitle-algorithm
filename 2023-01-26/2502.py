# 시간복잡도: O(N)
# 어려웠던 점: 규칙을 찾기까지 시간이 걸림

# 아이디어: 첫째 날의 개수를 A, 둘째 날의 개수를 B라고 할 때
# 다음 항에 포함된 A와 B의 개수가 피보나치 수열로 증가하는 것을 활용
# 한 항을 구하면 나머지 항도 구할 수 있음

D, K = map(int, input().split())
dp = [1, 1]

for i in range(2, D):
    dp.append(dp[i - 1] + dp[i - 2])

for i in range(1, K):
    n = i * dp[D - 3]
    if (K - n) % dp[D - 2] == 0:
        print(i)
        print((K - n) // dp[D - 2])
        break
