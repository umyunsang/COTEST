'''
<슈도코드 작성>
N(수열 개수) A(수열 리스트)
A 수열 리스트 채우기

for N만큼 반복:
    if 현재 수열값 >= 오름차순 자연수:
        while 현재 수열값 >= 오름차순 자연수:
            append()
            오름차순 자연수 1 증가
            (+)저장
        pop()
        (-)wjwkd
    else 현재 수열값 < 오름차순 자연수:
        pop()
        if 스택 pop 결과값 > 수열의 수:
            NO 출력
        else:
            (-)저장

if NO값을 출력한 적이 없으면:
    저장한 값 출력
'''
# 코드 구현
N = int(input())
A = [0] * N

for i in range(N):
    A[i] = int(input())

stack =[]
num = 1
result = True
answer = []

for i in range(N):
    su = A[i]
    if su >= num:   # 현재 수열값 >= 오름차순 자연수: 값이 같아질 때까지 append() 수행
        while su >= num:
            stack.append(num)
            num += 1
            answer.append('+')
        stack.pop()
        answer.append('-')
    else:   # 현재 수열값 < 오름차순 자연수: pop()을 수행해 수열 원소를 꺼냄
        n = stack.pop()
        # 스택의 가장 위의 수가 만들어야 하는 수열의 수보다 크면 수열을 출력할 수 없음
        if n > su:
            print("NO")
            result = False
            break
        else:
            answer.append('-')

if result:
    for i in answer:
        print(i)