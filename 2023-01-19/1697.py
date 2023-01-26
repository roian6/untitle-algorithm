# 시간복잡도: O(N*M)
# 어려웠던 점: 예전에 작성하여 비효율적인 코드가 있음

from collections import deque

# 아이디어: BFS를 통해 방문한 지점과 depth를 기록하여 풀 수 있음

N, K = map(int, input().split())

q = deque(iterable=(N,))
visited = [False] * 100001

ans = 0
while True:
    s = len(q)
    for _ in range(s):
        n = q.popleft()
        if n == K:
            print(ans)
            exit()
        for n2 in n - 1, n + 1, n * 2:
            if 0 <= n2 <= 100000 and not visited[n2]:
                q.append(n2)
                visited[n2] = True
    ans += 1
