def solution(my_string, overwrite_string, s):
    answer = ''
    for i in range(len(my_string)):
        if s <= i < s + len(overwrite_string):
            answer += overwrite_string[i - s]  # 올바르게 인덱스를 사용
        else:
            answer+=my_string[i]
    return answer