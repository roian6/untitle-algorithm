# 시간복잡도: O(N*M)
# 어려웠던 점: 예전에 작성하여 비효율적인 코드가 있음
from itertools import permutations, combinations_with_replacement

# 이이디어: 순열과 중복조합을 통해 모든 경우의 수를 구해 풀었었음
# 최적화할 부분이 많을 것으로 보임

N = int(input())
li = list(map(int, input().split()))

p = list(permutations(range(N)))

ans = 0
while True:
    ans += 1
    for t in combinations_with_replacement(range(len(p)), ans):
        arr = li.copy()
        for n in t:
            for i in range(N):
                arr[i] -= 3 ** (2 - p[n][i])
                arr[i] = max(arr[i], 0)
        if sum(arr) == 0:
            print(ans)
            break
    else:
        continue
    break
