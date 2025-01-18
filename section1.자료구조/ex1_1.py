'''
<슈도코드 작성>
n값 받기
numbers 변수에 list 함수를 이용하여 숫자를 한 자리씩 나누어 받기
sum 변수 선언

for numbers 탐색:
    sum 변수에 numbers에 있는 각 자리수를 가져와 더하기

sum 출력
'''
# 코드 구현
n = input()
nubmers = list(input())
sum = 0

for i in nubmers:
    sum = sum + int(i)  # numbers에 있는 각 자리 수를 가져와 더하기

print(sum)
