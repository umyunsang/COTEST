n = int(input())
count = 0

for i in range(1, n + 1):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        continue  # 2, 3, 5 중 하나로 나누어 떨어지면 건너뛰기
    count += 1  # 친근하지 않은 수 카운트

print(count)
