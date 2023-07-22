from collections import deque

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            move_x = x + dx[i]
            move_y = y + dy[i] 
            if move_x < 0 or move_x >= N or move_y < 0 or move_y >= M : continue

            if graph[move_x][move_y] == 0: continue
            
            if graph[move_x][move_y] == 1: #왜 if (move_x, move_y) not in queue:는 안될까?
                queue.append((move_x, move_y))
                graph[move_x][move_y] = graph[x][y] + 1
                
    return graph[N-1][M-1]

    
print(bfs(0, 0))
