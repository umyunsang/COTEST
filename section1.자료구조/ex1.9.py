'''
<슈도코드 작성>
# 전역 변수 선언
checkList(비밀번호 체크 리스트)
myList(현재 상태 리스트)
checkSecret(몇 개의 문자와 관련된 개수를 충족했는지 판단하는 변수)

# 함수 선언
myadd(문자 더하기 함수)
    myList에 새로운 값을 더하고 조건에 따라 checkSecret값 업데이트

myremove(문자 빼기 함수):
    myList에 새로운 값을 제거하ㅏ고 조건에 따라 checkSecret값 업데이트

# 메인 코드
S(문자열 크기) P(부분 문자열의 크기)
A(문자열 데이터)
checkList 데이터 받기
checkList를 탐색하여 값이 0인 데이터의 개수만큼 checkSecret 값 증가
# 값이 0이라는 것은 비밀번호 개수가 이미 만족되었다는 뜻
P 범위(0 ~ P-1)만큼 myList 및 checkSecret에 적용하고, 유효한 비밀번호인지 판단

for i를 P에서 S까지 반복:
    j 선언(i - P)
    # 이 부분은 myadd, myremove 함수로 별도 구현
    한 칸씩 이동하면서 제거되는 문자열과 새로 들어오는 문자열을 처리
    유효한 비밀번호인지(checkSecret == 4) 판단해 결과값을 업데이트

결과값 출력
'''
# 전역 변수 선언
checkList = [0] * 4
myList = [0] * 4
checkSecret = 0


# 함수 정의
def myadd(c):  # 새로 들어온 문자를 처리하는 함수
    global checkList, myList, checkSecret
    if c == 'A':
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecret += 1
    elif c == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif c == 'G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    elif c == 'T':
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1


def myremove(c):  # 제거되는 문자를 처리하는 함수
    global checkList, myList, checkSecret
    if c == 'A':
        if myList[0] == checkList[0]:
            checkSecret -= 1
        myList[0] -= 1
    elif c == 'C':
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1
    if c == 'G':
        if myList[2] == checkList[2]:
            checkSecret -= 1
        myList[2] -= 1
    if c == 'T':
        if myList[3] == checkList[3]:
            checkSecret -= 1
        myList[3] -= 1


S, P = map(int, input().split())
Result = 0
A = list(input())
checkList = list(map(int, input().split()))

for i in range(4):
    if checkList[i] == 0:
        checkSecret += 1

for i in range(P):  # 초기 P 부분 문자열 처리 부분
    myadd(A[i])

if checkSecret == 4:  # 4 자릴수와 관련된 크기가 모두 충족될 때 유효한 비밀번호
    Result += 1

for i in range(P, S):
    j = i - P
    myadd(A[i])
    myremove(A[j])
    if checkSecret == 4:
        Result += 1

print(Result)
