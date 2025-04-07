def solution(myString):
    answer = [0]
    n=0
    for str in myString:
        if str == 'x':
            n+=1
            answer.append(0)
        else:
            answer[n]+=1
    return answer