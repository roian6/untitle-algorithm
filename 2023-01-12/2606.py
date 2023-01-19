# 인접 행렬
# from collections import deque
#
# N = int(input())
# M = int(input())
#
# li = [[False for _ in range(N)] for _ in range(N)]
#
# for i in range(M):
#     A, B = map(int, input().split())
#     li[A - 1][B - 1] = li[B - 1][A - 1] = True
#
# q = deque()
# visited = set()
#
# q.append(0)
# visited.add(0)
#
# while q:
#     n = q.popleft()
#     for i in range(N):
#         if i not in visited and li[i][n]:
#             visited.add(i)
#             q.append(i)
#
# print(len(visited) - 1)

# 인접 리스트
from collections import deque

N = int(input())
M = int(input())

li = [[] for _ in range(N)]

for i in range(M):
    A, B = map(int, input().split())
    li[A - 1].append(B - 1)
    li[B - 1].append(A - 1)

q = deque()
visited = set()

q.append(0)
visited.add(0)

while q:
    n = q.popleft()
    for i in range(N):
        if i not in visited and n in li[i]:
            visited.add(i)
            q.append(i)

print(len(visited) - 1)
