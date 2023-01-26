# 시간복잡도: O(N*M)
# 어려웠던 점: 예전에 작성하여 비효율적인 코드가 있음

from collections import deque

F, S, G, U, D = map(int, input().split())

# 엘리베이터가 이동하지 않을 경우 예외처리
if (S < G and U == 0) or (S > G and D == 0):
    print('use the stairs')
    exit()

# 큐에 출발점을 넣고 방문 기록
q = deque(iterable=(S,))
visited = [False] * F
visited[S - 1] = True

# BFS 진행
ans = 0
while q:
    q2 = []
    while q:
        n = q.popleft()
        # 목표 층에 도달하면 정답 출력 후 종료
        if n == G:
            print(ans)
            exit()
        # 올라가는 경우, 내려가는 경우에 대해
        for m in (n + U, n - D):
            # 방문 가능하다면 방문 후 큐에 넣음
            if 0 < m <= F and not visited[m - 1]:
                visited[m - 1] = True
                q2.append(m)
    # depth 계산 및 기록
    q = deque(iterable=q2)
    ans += 1

print('use the stairs')
