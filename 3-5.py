N,K = map(int, input().split())
result = 0

#N을 최대한 k로 나누는 횟수 덧셈
while N>=K:
    N = int(N/K) + N%K
    result += 1

#만약 위 과정에서 값이 떨어지지 않는다면
#그 나머지 값만큼 -1과정을 진행한다는 가정하에, 횟수 덧셈
if N != 1:
    result += (N-1)

print(result)
