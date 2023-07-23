N = list(map(int, input()))

Half_index = int(len(N)/2)

Half_sum = sum = 0
for i in range(len(N)):
    if i == Half_index :
        Half_sum = sum
        sum = 0
    sum += N[i]

if Half_sum == sum: print("LUCKY")
else: print("READY")
