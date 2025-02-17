def solution(num_list):
    answer = 0
    odd=''
    even=''
    for num in num_list:
        if num % 2:
            odd+=str(num)
        else:
            even+=str(num)
    return int(odd)+int(even)