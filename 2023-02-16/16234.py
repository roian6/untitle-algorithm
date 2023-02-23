from sys import stdin
from collections import deque

input = stdin.readline
N, L, R = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(N)]

dy, dx = (0, -1, 0, 1), (-1, 0, 1, 0)

for ans in range(2000):
    visited = [[False] * N for _ in range(N)]
    q = deque()
    moved = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                v, su = [], 0
                q.append((i, j))
                visited[i][j] = True
                while q:
                    y, x = q.popleft()
                    v.append((y, x))
                    su += li[y][x]
                    for n in range(4):
                        ny, nx = y + dy[n], x + dx[n]
                        if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and L <= abs(li[y][x] - li[ny][nx]) <= R:
                            q.append((ny, nx))
                            visited[ny][nx] = True
                            moved = True
                cnt = len(v)
                for y, x in v:
                    li[y][x] = su // cnt
    if not moved:
        print(ans)
        break
