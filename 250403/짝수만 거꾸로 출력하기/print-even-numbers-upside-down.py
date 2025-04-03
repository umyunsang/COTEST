n = int(input())
result = list(map(int, input().split()))
result.reverse()

for i in range(n):
    if result[i] % 2 == 0:
        print(result[i], end=' ')
