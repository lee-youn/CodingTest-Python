# 동전 0 문제 풀이
N, K = map(int, input().split())
coins = [int(input()) for i in range(N)]
print(coins)

coins = sorted(coins, reverse=True)

count = 0
print(coins)

for i in coins:
    count += K // i
    K = K % i

print(count)