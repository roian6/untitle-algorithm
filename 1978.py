# 시간, 공간 복잡도: O(NloglogN), O(N) (문제에서 N은 1000)
# 어려웠던 점: 예전에 O(N^2)로 해결, 에라토스테네스 체 적용하여 최적화함
N = int(input())
li = list(map(int, input().split()))
MAX = 1000

# 에라토스테네스의 체로 소수 목록 구하기
p = [False, False] + [True for i in range(MAX - 1)]
for i in range(2, MAX + 1):
    if p[i]:
        for j in range(i ** 2, MAX + 1, i):
            p[j] = False

# 소수 개수 출력
print(sum(1 if p[n] else 0 for n in li))
