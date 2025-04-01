ran = int(input())
n = map(int, input().split())
print(" ".join(map(str, [x**2 for x in n])))