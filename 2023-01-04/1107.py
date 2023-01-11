# 시간, 공간 복잡도: O(N), O(1)
# 어려웠던 점: 예외처리 할 부분이 많았음

# 입력
N = int(input())
M = int(input())

# 고장나지 않은 버튼 구하기 (차집합)
nums = sorted(set(range(10)) - set(map(int, input().split()) if M else ()))

# 모든 버튼이 고장난 경우
if M == 10:
    # +-로만 채널 변경하는 횟수
    print(abs(N - 100))
    exit()
# 0을 제외한 버튼이 모두 고장난 경우
elif M == 9 and nums[0] == 0:
    # +-로만 채널 변경하는 횟수, 0을 누르고 올라가는 횟수 중 작은 값
    print(min(abs(N - 100), N + 1))
    exit()
# 버튼이 고장나지 않은 경우
elif M == 0:
    # +-로만 채널 변경하는 횟수, 직접 번호를 누르는 횟수 중 작은 값
    print(min(abs(N - 100), len(str(N))))
    exit()

# 아이디어: n진수(n은 고장나지 않은 버튼의 개수 + 1)를 활용하여 낮은 숫자부터 조합을 만듬
# 목표보다 작은 수 중 목표와 가장 가까운 수 up, 목표보다 큰 수 중 목표와 가장 가까운 수 down을 찾음
# +-로만 채널 변경하는 횟수, up을 누르고 올라가는 횟수, down을 누르고 내려가는 횟수 중 가장 작은 것이 정답

# n진수를 저장할 배열
li = [1] + [0] * 7

# up이 갱신되지 않는 상황을 대비해 -9로 초기화
up = -9
while True:
    # 현재 시도해볼 숫자 조합을 만듬
    n = i = 0
    while li[i]:
        n += nums[li[i] - 1] * pow(10, i)
        i += 1

    # 숫자 조합이 목표값보다 커지는 순간
    if n > N:
        # down을 기록하고 반복문 종료
        down = n
        break
    # 그렇지 않다면 up 갱신
    else:
        up = n

    # n진수 +1 연산
    li[0] += 1
    for i in range(7):
        if li[i] > len(nums):
            li[i] = 1
            li[i + 1] += 1
        else:
            break

# 계산한 up과 down에 따라 가장 효율적인 경우의 수 출력
print(min(abs(N - 100), len(str(up)) + N - up, len(str(down)) + down - N))
