from collections import deque
from sys import stdin

input = stdin.readline

N = int(input())
li = [list(input()) for _ in range(N)]

dy, dx = (-1, 0, 1, 0), (0, 1, 0, -1)
ans = [0, 0]
for t in range(2):
    q = deque()
    visited = [[False for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue

            q.append((i, j))
            visited[i][j] = True

            c = li[i][j]
            if li[i][j] == 'R':
                li[i][j] = 'G'

            while q:
                y, x = q.popleft()
                for k in range(4):
                    ny, nx = y + dy[k], x + dx[k]
                    if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and li[ny][nx] == c:
                        q.append((ny, nx))
                        visited[ny][nx] = True
                        if li[ny][nx] == 'R':
                            li[ny][nx] = 'G'
            ans[t] += 1

print(ans[0], ans[1])
