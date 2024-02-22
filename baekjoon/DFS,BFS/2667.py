# 2667 단지번호 붙이기 문제


N = int(input())

numbers = []

for i in range (N):
    input_number = list(map(int, input()))
    numbers.append(input_number)

print(numbers)

count = []
count_house = 0

def dfs(x,y):
    global count_house

    if x < 0 or x >= N :
        if y < 0 or y >= N :
            return False

    if numbers[x][y] == 1:
        numbers[x][y] = 0
        count_house += 1
        print(count_house)
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x, y+1)
        return True
    return False

for i in range(N):
    for j in range(N):
        if dfs(i,j) == True:
            print(count)
            print(count_house)
            count.append(count_house)
            count_house = 0

count.sort()

print(len(count))

for i in range(len(count)):
    print(count[i])
