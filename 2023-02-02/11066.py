# 시간복잡도: O(N^3)
# 어려웠던 점: 그냥 어렵다. O(N^3) 풀이로는 파이썬으로 통과할 수 없다.

from sys import stdin

input = stdin.readline
T = int(input())

# 아이디어: https://js1jj2sk3.tistory.com/search/11066

for _ in range(T):
    K, li = int(input()), list(map(int, input().split()))

    # 파일 크기의 누적합을 저장
    su = [0] * (K + 1)
    for i in range(K):
        su[i + 1] = li[i] + su[i]

    # dp[i][j]는 i번째 장부터 j번째 장까지 합치는 최소 비용
    dp = [[0] * (K + 1) for _ in range(K + 1)]

    # 1~2, 2~3 ... / 1~3, 2~4 ... / ... / 1~K 까지 돌면 끝
    for i in range(1, K):
        for st in range(1, K - i + 1):
            en = i + st
            # mid를 기준으로 두 그룹으로 나눠서
            # 왼쪽 그룹 만드는 최소 비용 + 오른쪽 그룹 만드는 최소 비용 + 두개 합치는 비용 중
            # 가장 작은 값을 dp에 기록
            dp[st][en] = min([dp[st][mid] + dp[mid + 1][en] + su[en] - su[st - 1] for mid in range(st, en)])

    # 1~K까지 합치는 최소 비용(정답)
    print(dp[1][K])
