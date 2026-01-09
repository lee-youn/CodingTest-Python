# 2573 빙산 문제 풀이
from collections import deque

N,M  = map(int, input().split())
graph = []
for i in range(N):
    arr = list(map(int, input().split()))
    graph.append(arr)

visited = [[False] * M for _ in range(N)]

dirs = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs(graph, start, visited):
    queue = deque([start]) # start가 (x, y) 튜플이면 deque(start)는 x, y 두 원소를 각각 큐에 넣는다;;
    # print(queue)
    visited[start[0]][start[1]] = True 

    while queue:
        c = queue.popleft()
        for dx, dy in dirs:
            nx = c[0] + dx
            ny = c[1] + dy

            if not (0 <= nx < N and 0 <= ny < M):
                continue
            state = graph[nx][ny]
            if state <= 0:
                continue
            if not visited[nx][ny]:
                queue.append((c[0]+dx, c[1]+dy))
                visited[c[0]+dx][c[1]+dy] = True

year_count = 0
coords = [(i, j) for i in range(N) for j in range(M) if graph[i][j] > 0]

while True:
    # print(coords)
    if coords == []:
        year_count = 0
        break
    else:
        visited = [[False] * M for _ in range(N)]
        bfs(graph, coords[0], visited)

        if any(graph[i][j] > 0 and not visited[i][j] for (i, j) in coords):
            # print(year_count)
            break
        
        melted = [[0] * M for _ in range(N)]
        for x, y in coords:
            sea = 0
            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < N and 0 <= ny < M:
                    if graph[nx][ny] == 0:
                        sea += 1
            melted[x][y] = sea


        # new_graph = [row[:] for row in graph] 
        # for x in range(N):
        #     for y in range(M):
        #         if graph[x][y] > 0:
        #             new_graph[x][y] = max(0, graph[x][y] - melted[x][y])

        # graph = new_graph
        # new_graph = [row[:] for row in graph] 
        new_coords = []
        for idx, (x, y) in enumerate(coords):
            nh = graph[x][y] - melted[x][y]
            if nh > 0:
                graph[x][y] = nh
                new_coords.append((x, y))
            else:
                graph[x][y] = 0

        coords = new_coords
        year_count += 1

        # graph = new_graph
        # print(graph)
        # print(visited

print(year_count)