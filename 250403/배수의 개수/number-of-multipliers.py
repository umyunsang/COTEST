result_3,result_5 = 0,0
for _ in range(10):
    i = int(input())
    if i % 5 == 0: result_5 += 1
    if i % 3 == 0: result_3 += 1
print(f'{result_3} {result_5}')