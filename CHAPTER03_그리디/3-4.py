# 3-3 숫자 카드 게임
N,M = map(int, input().split())

matrix = [list(map(int, input().split())) for i in range(N)]
max_of_minimums = 0

for i in range(N) :
    if max_of_minimums < min(matrix[i]): 
        max_of_minimums = min(matrix[i])

print(max_of_minimums)
