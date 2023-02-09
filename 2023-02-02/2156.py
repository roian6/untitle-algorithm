# 시간복잡도: O(N)
# 어려웠던 점: O(N)인걸 깨닫기까지 시간이 걸림

from sys import stdin

input = stdin.readline
N = int(input())
li = [0] * 3
for i, n in enumerate([int(input()) for _ in range(N)]):
    li[i % 3] = max(li)
    li[(i + 1) % 3] += n
    li[(i + 2) % 3] += n

print(max(li))
