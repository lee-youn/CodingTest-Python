#3-2 문제풀이

N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))

# 리스트 정렬
numbers.sort()

# 최대 연속 가능 수 만큼 큰 수를 더하고,
# 연속 수 사이 사이로 두번째로 큰 수를 더함
maximum_number = N-1
result = 0
maximum_number_count = M-int(M/K)

for i in range(maximum_number_count):
    result += numbers[maximum_number]

for i in range(int(M/K)):
    result += numbers[maximum_number-1]

print(result)