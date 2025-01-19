'''
<슈도 코드 작성>
n 변수 저장
사용 변수 초기화(count=1, start_index=1, end_index=1, sum=1)

while end_index != n:
    if summ == n: 경우의 수 증가, end_index 증가, sum값 변경
    elif sum > n: sum값 변경, star_index 증가
    else: end_index 증가, sum값 변경

경우의 수 출력
'''
# 코드 구현
n = int(input())
count = 1
start_index = 1
end_index = 1
sum = 1

while end_index != n:
    if sum == n:    # 정답 케이스
        count += 1
        end_index += 1
        sum += end_index
    elif sum > n:
        sum -= start_index
        start_index += 1
    else:
        end_index += 1
        sum += end_index

print(count)