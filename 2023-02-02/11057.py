# 시간복잡도: O(N)
# 어려웠던 점: O(N)인걸 깨닫기까지 시간이 걸림

N = int(input())
li = [1] * 10
for _ in range(N - 1):
    for i in range(9):
        li[i + 1] += li[i]
print(sum(li) % 10007)
