'''
<슈도코드 작성>
N(질의 요청 개수)
우선순위 큐 선언
- 절댓값 기준으로 정렬되도록 설정
- 단, 절댓값이 같으면 음수 우선 정렬

for N만큼 반복:
    요청이 0일 때: 큐가 비어 있으면 0, 비어 있지 않으면 큐의 front값 출력(get())
    요청이 1일 때: 새로운 데이터를 우선순위 큐에 더하기(put())
'''
import sys
from queue import PriorityQueue

# 코드 구현
print = sys.stdout.write
input = sys.stdin.readline
N = int(input())
myQueue = PriorityQueue()

for i in range(N):
    request = int(input())
    if request == 0:
        if myQueue.empty():
            print('0\n')
        else:
            temp = myQueue.get()
            print(str((temp[1]))+'\n')
    else:
        # 절대값을 기준으로 정렬하고 같으면 음수 우선 정렬하도록 구성
        myQueue.put((abs(request),request))