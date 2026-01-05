# 23971 ZOAC 4 문제
def solution (h, w, n, m):
    down = (h+n+1-1) // (n+1)
    right = (w+m+1-1) // (m+1)

    return down * right

h, w, n, m = map(int, input().split())
print(solution(h,w,n,m))