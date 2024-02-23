# 2667 단지번호 붙이기 문제


N = int(input())

numbers = []

for i in range (N):
    input_number = list(map(int, input()))
    numbers.append(input_number)


count = []
count_house = 0

def dfs(x,y):
    global count_house

    if x < 0 or x >= N or y < 0 or y >= N :
        return

    if numbers[x][y] == 1:
        numbers[x][y] = 0
        count_house += 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x, y+1)
        return True

for i in range(N):
    for j in range(N):
        if numbers[i][j] == 1:
            dfs(i,j)
            count.append(count_house)
            count_house = 0

count.sort()

print(len(count))

for i in range(len(count)):
    print(count[i])
