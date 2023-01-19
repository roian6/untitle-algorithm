# 시간복잡도: O(N*M)
# 어려웠던 점: 예전에 작성하여 비효율적인 코드가 있음

from sys import stdin
from collections import deque

# 입력 및 BFS에 필요한 변수 선언
M, N = map(int, stdin.readline().split())
li = []
for i in range(N):
    li.append(list(map(int, stdin.readline().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

ans = 0
tomato = deque()
for i in range(N):
    for j in range(M):
        if li[i][j] == 1:
            tomato.append((i, j))

# BFS를 여러 번 하며 depth 기록 후 출력
while tomato:
    q = deque()
    while tomato:
        x, y = tomato.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if li[nx][ny] == 0:
                    li[nx][ny] = 1
                    q.append((nx, ny))
    ans += 1
    tomato = q
ans -= 1

# 익지 않은 토마토가 있다면 실패
for li2 in li:
    if 0 in li2:
        ans = -1
        break

print(ans)
