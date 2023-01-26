# 시간복잡도: O(N*M)
# 어려웠던 점: 예외처리가 힘들었음

from collections import deque
from sys import stdin

# 입력
input = stdin.readline
N, M = map(int, input().split())
li = [list(map(int, list(input().strip()))) for _ in range(N)]

# 아이디어: BFS을 진행하되 각 시도마다 한번씩 벽을 부술 수 있게 함
# 이때 벽을 부순 시도에서 방문했던 곳은 벽을 부수지 않은 시도에서 다시 방문할 수 있도록 함

# 아이디어 2: 모든 벽에 대해 (1, 1), (N, M)으로 각각 BFS 진행 후 거리의 합을 구함
# 이중 가장 작은 것이 정답이 됨 (이 방법이 더 효율적이라고 생각)

# BFS에 사용할 좌표, 최단거리 기록 변수 선언
dy, dx = (-1, 0, 1, 0), (0, 1, 0, -1)
ans = 1

# 큐에 좌표와 함께 벽을 부술 수 있는지 여부를 함께 저장
q = deque(iterable=((0, 0, True),))

# 벽을 부수지 않은 시도에서 방문한 곳은 2, 부순 시도에서 방문한 곳은 1로 기록
visited = [[0 for _ in range(M)] for _ in range(N)]
visited[0][0] = 2

while q:
    # BFS 깊이 계산을 위해 큐 크기 기록
    s = len(q)
    for _ in range(s):
        # 큐에서 좌표와 벽을 부술 수 있는지 여부를 가져옴
        y, x, b = q.popleft()
        # 목표 지점에 도달했다면 현재 최단거리 출력 후 종료
        if y == N - 1 and x == M - 1:
            print(ans)
            exit()
        # 상하좌우 좌표 검사
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                # 좌표가 이동할 수 있는 곳이라면
                if not li[ny][nx]:
                    # 벽을 부수지 않은 시도이고 다른 벽을 부수지 않은 시도에서 방문하지 않았다면 2,
                    # 벽을 부순 시도이고 이전에 방문하지 않았다면 1을 visited에 기록 후 큐에 값을 넣음
                    if b and visited[ny][nx] < 2:
                        q.append((ny, nx, b))
                        visited[ny][nx] = 2
                    elif not visited[ny][nx]:
                        q.append((ny, nx, b))
                        visited[ny][nx] = 1
                # 좌표가 벽이고 아직 벽을 부수지 않은 시도라면
                elif b and not visited[ny][nx]:
                    # 벽을 부쉈음을 기록, visited에 1을 넣음
                    q.append((ny, nx, False))
                    visited[ny][nx] = 1
    # BFS의 깊이(최단거리) 기록
    ans += 1

# 목표지점에 도달하지 못하면 -1 출력
print(-1)
