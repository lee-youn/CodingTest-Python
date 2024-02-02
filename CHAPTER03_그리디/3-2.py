#3-2 문제풀이

N,M,K = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort(reverse=True) #역정렬
Max_number=0

#두번째로 큰 수가 반복되는 횟수 계산
repeat = M%K
Max_number += (M-repeat)*numbers[0] #첫번째 큰 수 횟수만큼 덧셈
Max_number += (repeat)*numbers[1] #두번째 큰 수 횟수만큼 덧셈

print(Max_number)
