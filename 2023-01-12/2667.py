# 시간복잡도: O(N*M)
# 어려웠던 점: 예전에 작성하여 비효율적인 코드가 있음

from collections import deque
from sys import stdin

# 입력 및 BFS에 필요한 변수 선언
N = int(stdin.readline())
m = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(N):
    m.append(list(map(int, stdin.readline().strip())))

# BFS 진행
def bfs(g, a, b):
    n = len(g)
    q = deque()
    q.append((a, b))
    g[a][b] = 0
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 방문한 위치는 0으로 초기화
            if 0 <= nx < n and 0 <= ny < n:
                if m[nx][ny] == 1:
                    g[nx][ny] = 0
                    q.append((nx, ny))
                    cnt += 1
    return cnt


ans = []
for i in range(N):
    for j in range(N):
        if m[i][j] == 1:
            ans.append(bfs(m, i, j))

# 정렬 후 출력
print(len(ans))
ans.sort()
for n in ans:
    print(n)
