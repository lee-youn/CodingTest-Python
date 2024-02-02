N = int(input())

person = list(map(int, input().split()))

person.sort(reverse = True)

number = 0
group = 0

while True:
    if number >= N : break
    index = number
    for j in range(person[index]):
        number += 1
    group += 1

print(group)
