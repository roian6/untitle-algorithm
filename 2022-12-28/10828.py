# 시간, 공간 복잡도: O(N), O(N)
# 어려웠던 점: 기본 자료형인 list를 사용했으나 직접 구현하는 방법도 공부할 것
from sys import stdin

N = int(stdin.readline())
li = []

# 입력받은 명령어에 따라 동작 수행하기
for i in range(N):
    s = stdin.readline()
    if 'pu' in s:
        li.append(s.split()[1])
    elif 'po' in s:
        print(li.pop() if len(li) else -1)
    elif 'si' in s:
        print(len(li))
    elif 'em' in s:
        print(0 if len(li) else 1)
    elif 'to' in s:
        print(li[-1] if len(li) else -1)
