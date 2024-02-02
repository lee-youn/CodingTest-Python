Y, X=map(str, input())

#문자열로 입력받고, 아스키코드 값으로 변환
x = ord(X)-48
y = ord(Y)-96

count = 0

#나이트가 이동할 수 있는 경우의 수
motions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

for move in motions:
    x_move = x + move[0]
    y_move = y + move[1]
    if x_move > 0 and x_move <= 8 and y_move > 0 and y_move <= 8: count += 1


print(count)
