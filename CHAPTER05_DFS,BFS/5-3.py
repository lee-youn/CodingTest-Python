N, M = map(int, input().split())

ice_graph = []
count = 0

for i in range(N):
    for j in range(M):
        hole = int(input())
        ice_graph.append(hole)

def dfs(i,j):
    if i
    

for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            count += 1