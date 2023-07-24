from collections import deque

N, M, K, X = map(int, input().split())

link = [[] for i in range(N+1)]

for i in range(M):
    x, y = map(int, input().split())
    link[x].append(y)

count = [1] * (N+1)
count[0] = count[X] = 0

def bfs(x):
    node = [False] * (N+1)
    departure = X
    queue = deque(link[x])
    while queue:
        city = queue.popleft()
        node[city] = True
        departure = city
        for i in link[city]:
            if i in list(queue): continue
            else:
                queue.append(i)
                node[i] = True
                count[i] = count[departure]+1
                
    if K not in count: print(-1)
    else:
        for i in range(N+1):
            if count[i] == K: 
                print(i)
  
bfs(X)
