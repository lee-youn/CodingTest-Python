N = input()
location = list(map(str, input().split()))

X,Y=1,1

for i in location:
    if X==1 and i=='U': continue
    elif X==N and i=='R': continue
    elif Y==1 and i=='L': continue
    elif Y==N and i=='D': continue
    if i=='U': X -= 1
    if i=='R': Y += 1
    if i=='L': Y -= 1
    if i=='D': X += 1

print(X, Y)
