def solution(myString):
    answer = ''
    for i in myString:
        if i == 'a' or i == 'A':
            answer += 'A'
        elif i.isupper():
            answer += i.lower()
        else:
            answer += i
    return answer