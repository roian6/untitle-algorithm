# 시간복잡도: O(N*M)
# 어려웠던 점: 예전에 작성하여 비효율적인 코드가 있음

from collections import deque
from sys import stdin

# 입력 및 BFS에 필요한 큐, 방문 기록 선언
MAX = 101
N, M = map(int, stdin.readline().split())
ans = [[0 for _ in range(MAX)] for _ in range(MAX)]
visited = [[False for _ in range(MAX)] for _ in range(MAX)]
m = [[] for _ in range(MAX)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
q = deque()

for i in range(N):
    s = input()
    for s1 in s:
        m[i].append(s1)

# 초기 위치를 큐에 넣고 BFS 진행
visited[0][0] = True
q.append((0, 0))
while len(q) > 0:
    u = q.popleft()
    x = u[0]
    y = u[1]

    for i in range(4):
        nx = u[0] + dx[i]
        ny = u[1] + dy[i]

        # 방문한 지점에 현재 지난 칸 수를 남김
        if 0 <= nx < N and 0 <= ny < M:
            if m[nx][ny] == '1' and not visited[nx][ny]:
                ans[nx][ny] = ans[x][y] + 1
                visited[nx][ny] = True
                q.append((nx, ny))

print(ans[N - 1][M - 1] + 1)
