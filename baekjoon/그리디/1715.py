# 1715 카드 정렬하기 문제

import heapq

N = int(input())
number_card = []
for i in range(N) :
    number_size = int(input())
    heapq.heappush(number_card, number_size)

sum = 0

while len(number_card) > 1:
    val1 = heapq.heappop(number_card)
    val2 = heapq.heappop(number_card)
    result = val1 + val2
    sum += result
    heapq.heappush(number_card, result)
    #if len(number_card) == 1: break

print(sum)