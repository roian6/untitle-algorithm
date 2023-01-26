# 시간복잡도: O(N*M)
# 어려웠던 점: 예전에 작성하여 비효율적인 코드가 있음
from collections import deque

N, K = map(int, input().split())

# 아이디어: BFS를 통해 방문 로그를 기록, 목표지점 도달 시 방문 로그의 길이 출력
# 방문한 위치를 기록하지 않는 방식으로 최적화가 가능할 것 같음

if N >= K:
    print(N - K)
    exit()

visited = [0] * 100001
level = 0

q = deque()
q.append((0,))
q.append((1,))
q.append((2,))

while q:
    t = q.popleft()
    n = N
    for i, b in enumerate(t):
        if b == 0:
            n += 1
        elif b == 1:
            n -= 1
        else:
            n *= 2

        if 0 < n <= 100000 and (not visited[n - 1] or visited[n - 1] >= (i + 1)):
            visited[n - 1] = i + 1
            if n == K:
                print(len(t))
                exit()
        elif n > 100000 and n - 100000 <= len(t) - (i + 1):
            continue
        else:
            break
    else:
        q.append(t + (0,))
        q.append(t + (1,))
        q.append(t + (2,))
