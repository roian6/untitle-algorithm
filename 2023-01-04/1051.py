# 시간, 공간 복잡도: O(N^3), O(N^2)
# 어려웠던 점: 시간 복잡도를 N^3이라고 봐야 하는지 의문

# 입력
N, M = map(int, input().split())
li = [input() for i in range(N)]

# 정사각형의 크기를 최대(min(N, M))로 잡고 1씩 줄여 가며 검사
for s in range(min(N, M), -1, -1):
    # 크기에 해당하는 모든 정사각형을 검사
    for i in range(N - s):
        for j in range(M - s):
            # 네 꼭짓점이 모두 같다면 크기 출력 후 종료
            if li[i][j] == li[i][j + s] == li[i + s][j] == li[i + s][j + s]:
                print((s + 1) ** 2)
                exit()
