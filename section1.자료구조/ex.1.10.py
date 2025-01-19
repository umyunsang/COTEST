'''
<슈도코드 작성>
N(데이터 개수) L(최소값을 구하는 범위)
mydeque(데이터를 담을 덱 자료구조)
now(주어진 숫자 데이터를 가지는 리스트)

for N만큼 반복:     # now 리스트를 탐색 (now[i]를 현재 값으로 세팅)
    덱의 마지막 위치에서부터 현재 값보다 큰 값은 덱에서 제거
    덱의 마지막 위치에 현재 값 저장
    덱의 1번째 위치에서부터 L의 범위를 벗어난 값(now index-L <= index)을 덱에서 제거
    덱의 1번째 데이터 출력
'''
from collections import deque

# 코드 구현
N, L = map(int, input().split())
mydeque = deque()
now = list(map(int, input().split()))

# 새로운 값이 들어올 때마다 정렬 대신 현재 수보다 큰 값을 덱에서 제거해 시간 복잡도를 줄임
for i in range(N):
    while mydeque and mydeque[-1][0] > now[i]:
        mydeque.pop()
    mydeque.append((now[i], i))
    if mydeque[0][1] <= i - L:
        mydeque.popleft()
    print(mydeque[0][0], end=' ')
