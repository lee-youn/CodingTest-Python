# 4-3 왕실의 나이트

str_number = input()
row= ord(str_number[0]) - 96
column= int(str_number[1])

move = [(1,2), (1,-2), (-1,2), (-1,-2), (2,1), (2,-1), (-2,1), (-2,-1)]
count = 0

for i in move:
    move_column = i[0]
    move_row = i[1]
    if (row + move_row) >= 1 and (row + move_row) <= 8:
        if (column+ move_column) >= 1 and (column+ move_column) <= 8:
            count += 1

print(count)