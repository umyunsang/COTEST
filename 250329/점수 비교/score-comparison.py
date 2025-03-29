A_math, A_eng = map(int, input().split())
B_math, B_eng = map(int, input().split())

print(1 if A_math > B_math and A_eng > B_eng else 0);