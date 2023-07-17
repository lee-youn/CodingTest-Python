N,M = map(int, input().split())

min_number = 0
for i in range(N):
    data = list(map(int, input().split()))
    #가장 작은 수들 중에서 가장 큰 수 찾기기
    if min_number <= min(data):             #min_number = max(min_number, min(data))
        min_number = min(data)
    
print(min_number)
