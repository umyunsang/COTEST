result = list(map(int, input().split()))
for _ in range(8):
    result.append((result[-1] + result[-2]) % 10)

for i in result:
    print(i, end=' ')