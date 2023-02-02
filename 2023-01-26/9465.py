# 시간복잡도: O(N)
# 어려웠던 점: O(N)인걸 깨닫기까지 시간이 걸림

# 아이디어: 스티커를 떼지 않는 경우, 위쪽, 아래쪽 스티커를 떼는 경우 3가지의 선택지를 기록
# 앞에 선택한 선택지를 못 고를 뿐 사실상 그리디라고 생각해도 괜찮을 듯

from sys import stdin

input = stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    li = [[0] * n] + [list(map(int, input().split())) for _ in range(2)]

    for i in range(n - 1):
        for c in range(3):
            li[c][i + 1] += max(li[c - 2][i], li[c - 1][i])

    print(max([li[1][-1], li[2][-1]]))
