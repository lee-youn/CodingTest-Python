# N = int(input())
# weight =list(map(int, input().split()))
# sorted_weight = sorted(weight, reverse=True)

# for i in range(len(sorted_weight)):
#     remain_sorted_weight = sum(sorted_weight[i+1:])
#     if (sorted_weight[i] <= remain_sorted_weight) and remain_sorted_weight in sorted_weight:
#         continue
#     else:
#         print(remain_sorted_weight + 1)
#         break

# sum을 매번하는 것은 효율에 안좋음 0(N^2)

N = int(input())
weights = list(map(int, input().split()))
weights.sort() 

reach = 0
for i in weights:
    if i > reach + 1:
        break
    else:
        reach += i

print(reach + 1)