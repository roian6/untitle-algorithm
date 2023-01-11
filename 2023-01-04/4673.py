# 시간, 공간 복잡도: O(N), O(N)
# 어려웠던 점: 생성자가 있는 수 기록과 셀프 넘버 출력을 동시에 해서 반복문을 줄임

# 셀프 넘버 여부를 저장할 배열
li = [True] * 10036

for i in range(1, 10001):
    # 생성자가 있는 수는 false로 변경
    li[i + sum(map(int, str(i)))] = False

    # 셀프 넘버라면 출력
    if li[i]:
        print(i)
