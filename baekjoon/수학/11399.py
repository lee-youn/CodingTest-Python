# 11399 ATM 문제

N = int(input())
P = list(map(int, input().split()))

P.sort()
result = 0

for i in P:
    result += i*N
    N -= 1

print(result)