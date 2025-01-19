'''
<슈도코드 작성>
N(카드의 개수) myQueue(카드 저장 자료구조)

for 카드의 개수만큼 반복:
    큐에 카드 저장

while 카드가 1장 남을 떄까지:
    맨 위의 카드를 버림: popleft()
    맨 위의 카드를 가장 아래의 카드 밑으로 이동: popleft() -> append()

마지막으로 남은 카드 출력
'''
from collections import deque

# 코드 구현
N = int(input())
myQueue = deque()

for i in range(1, N+1):
    myQueue.append(i)

while len(myQueue) > 1:     # 카드가 1장 남을 때까지
    # 맨 위의 카드를 버림
    myQueue.popleft()
    # 맨 위의 카드를 가장 아래 카드 밑으로 이동
    myQueue.append(myQueue.popleft())

print(myQueue[0])   # 마지막으로 남은 카드 출력