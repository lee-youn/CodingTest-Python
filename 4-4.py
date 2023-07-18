N, M = map(int, input().split())
A, B, d = map(int, input().split())


matrix = [list(map(int, input().split())) for _ in range(N)]

check = [[0] * M for _ in range(N+1)]
check[A][B] = 1
stop = 0
count = 1

motion = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def turn_left():
    global d
    d -= 1
    if d == -1: d = 3
    
while True:
    turn_left()
    a = A + motion[d][0]
    b = B + motion[d][1]
    if check[a][b] == 0 and matrix[a][b] == 0:
        check[a][b] = 1
        A = a 
        B = b 
        count += 1
        stop = 0
        continue
    else:
        stop += 1 
    
    if stop == 4:
        if matrix[A - motion[d][0]][B - motion[d][1]] == 0:
            A = A - motion[d][0]
            B = B - motion[d][1]
        else:
            break
        stop = 0

print(count)
