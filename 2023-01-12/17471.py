# 시간 복잡도: O(2^N)
# 어려웠던 점: 아이디어가 바로 떠오르지 않았음

from itertools import combinations
from collections import deque
from sys import stdin

# 입력
input = stdin.readline
N = int(input())
people = list(map(int, input().split()))

# 연결 관계를 인접리스트 형태로 저장
# [{2, 4}, {1, 3, 6, 5}, {4, 2}] 이런 식으로 저장됨
table = [set(n - 1 for n in map(int, input().split()[1:])) for _ in range(N)]

# 아이디어: 조합을 이용하여 구역들을 2개의 선거구로 나누는 모든 경우를 테스트해봄
# 각각의 선거구에서 하나씩의 구역을 뽑아 BFS (같은 선거구 내에서만)
# 모든 구역을 방문했다면 성공, 각 선거구의 인구를 계산해 최소 인구 차이를 정답으로 기록

ans = -1
for i in range(1, N):
    # 구역들 중 i개를 뽑아 조합을 만듬 (s1, 선거구 1)
    for s1 in map(set, combinations(range(N), i)):
        # 차집합을 이용해 선거구 1을 제외한 구역들로 조합을 만듬 (s2, 선거구 2)
        s2 = set(range(N)) - s1

        # BFS를 위한 큐와 방문 기록 선언
        q = deque()
        visited = set()

        # 선거구 1, 2에 각각 아래 작업을 진행
        for s in s1, s2:
            # 선거구에서 아무 구역이나 하나 뽑아 큐에 넣음
            start = next(iter(s))
            visited.add(start)
            q.append(start)

            # BFS
            while q:
                cur = q.popleft()  # 큐에서 정점을 뽑는다
                for nxt in table[cur]:  # 연결된 모든 정점들에 대해
                    if nxt in s and nxt not in visited:  # 같은 선거구에 있고 방문하지 않았다면 큐에 넣음
                        q.append(nxt)
                        visited.add(nxt)

        # 모든 정점을 방문했다면 (두 선거구로 나누기 성공)
        if len(visited) == N:
            # 인구수 차이를 계산해 정답을 갱신
            score = abs(sum(people[n] for n in s1) - sum(people[n] for n in s2))
            if ans == -1 or score < ans:
                ans = score
print(ans)
