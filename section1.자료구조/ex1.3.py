'''
<슈도코드 작성>
suNo(숫자 개수), quizNo(질의 개수)
numbers 변수에 숫자 데이터 저장
prefix_sum 합 배열 변수 선언
temp 변수 선언

for 저장한 숫자 데이터 차례대로 탐색:
    temp에 현재 숫자 데이터 더해 주기
    합 배열에 temp값 저장

for 질의 개수만큼 반복:
    질의 범위 받기(s ~ e)
    구간 합 출력하기(prefix_sum[e] - prefix_sum[s-1])
'''
import sys

# 코드 구현
input = sys.stdin.readline
suNo, quizNo = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0]
temp = 0

for i in numbers:
    temp += i
    prefix_sum.append(temp)                 # 합 배열 만들기

for i in range(quizNo):
    s, e = map(int, input().split())
    print(prefix_sum[e]-prefix_sum[s-1])    # 합 배열에서 구간 합 구하기