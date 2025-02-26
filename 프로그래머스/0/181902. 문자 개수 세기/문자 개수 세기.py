def solution(my_string):
    answer = [int(0) for _ in range(52)]
    for i in my_string:
        if ord(i)>96:
            answer[ord(i)-71]+=1
        else:
            answer[ord(i)-65]+=1
    
    return answer