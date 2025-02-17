def solution(l, r):
    answer = []
    for i in range(1, 64):
        a = int(format(i, 'b'))*5
        if l <= a <= r:
            answer.append(a)
            
    return answer if answer else [-1]