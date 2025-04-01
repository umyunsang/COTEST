n = list(input())
n[1], n[-2] = 'a', 'a'
print(''.join(n))
