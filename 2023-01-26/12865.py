# 시간복잡도: O(N^2)
# 어려웠던 점: 점화식 세우기 정말 힘든 문제

# 아이디어: 1번 물건부터 마지막 물건까지 배낭의 무게를 1부터 K까지 늘려 보면서 물건이 배낭 안에 들어간다면,
# '물건을 안 넣는 경우의 가치' '배낭의 여유 공간을 물건의 무게 만큼 제했을 때의 최대 가치 + 물건을 넣어서 얻는 가치' 중 큰 것을 기록
# 마지막 물건을 K 크기에 배낭에 넣는 시도의 결과가 정답이 됨

from sys import stdin

input = stdin.readline
N, K = map(int, input().split())
# 가로 K+1, 세로 N+1 크기의 배열
dp = [[0] * (K + 1) for _ in range(N + 1)]

# 1번 물건부터 마지막 물건까지
for i in range(1, N + 1):
    # 물건의 무게와 가치 입력
    W, V = map(int, input().split())
    # 배낭의 크기를 1씩 늘려보며
    for j in range(1, K + 1):
        # 물건이 배낭의 크기보다 크다면, 같은 크기의 배낭에 이전 물건까지만 넣었을 때의 값을 그대로 가져옴
        # 배낭 안에 넣을 수 있다면 위의 아이디어대로 진행
        dp[i][j] = dp[i - 1][j] if W > j else max(dp[i - 1][j], dp[i - 1][j - W] + V)

# 마지막 물건을 K 크기의 배낭에 넣는 시도의 결과
print(dp[-1][-1])