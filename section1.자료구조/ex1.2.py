'''
<슈도코드 작성>
n에 과목의 수 입력
mylist에 점수 정보 저장
mymax에 mylist 정보 중 최댓값 저장
sum에 mylist 모든 데이터 값 더하기
sum * 100 / mymax / n 출력
'''
# 코드 구현
n = input()
mylist = list(map(int, input().split()))
mymax = max(mylist)
sum = sum(mylist)

print(sum * 100 / mymax / int(n))