# 1157 단어 공부 문제

word = input()
upper_case_char = []
alphabet_count = {}
max_count_alphabet = 0

for i in range(len(word)) :
    if ord(word[i]) >= 97:
        upper_case_char.append(chr(ord(word[i]) - 32))
    else:
        upper_case_char.append(word[i])
    alphabet_count[upper_case_char[i]]= alphabet_count.get(upper_case_char[i], 0) + 1

for i in alphabet_count :
    if alphabet_count[i] == max(alphabet_count.values()):
        max_count_alphabet += 1

if max_count_alphabet == 1 : 
    result_keys = [key for key, value in alphabet_count.items() if value == max(alphabet_count.values())]
    print(result_keys[0])
else :
    print("?")