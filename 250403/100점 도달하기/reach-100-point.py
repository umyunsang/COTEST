n = int(input())
while n != 101:
    print('A' if n >=90 else 'B' if n>=80 else 'C' if n>= 70 else 'D' if n>=60 else 'F', end=' ')
    n += 1

