from sys import stdin
from collections import deque

M, N, H = map(int, stdin.readline().split())
li = [[list(map(int, stdin.readline().split())) for _ in range(N)] for _ in range(H)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dh = [-1, 1]

ans = 0
tomato = deque()
for h in range(H):
    for i in range(N):
        for j in range(M):
            if li[h][i][j] == 1:
                tomato.append((h, i, j))

while tomato:
    s = len(tomato)
    for _ in range(s):
        h, x, y = tomato.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and not li[h][nx][ny]:
                li[h][nx][ny] = 1
                tomato.append((h, nx, ny))
        for k in range(2):
            nh = h + dh[k]
            if 0 <= nh < H and not li[nh][x][y]:
                li[nh][x][y] = 1
                tomato.append((nh, x, y))
    ans += 1
ans -= 1

for li2 in li:
    for li3 in li2:
        if 0 in li3:
            ans = -1
            break

print(ans)
