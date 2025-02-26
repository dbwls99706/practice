def solution(my_string, is_suffix):
    suf = []
    for i in range(len(my_string)):
        suf.append(my_string[i:])
    return 1 if is_suffix in suf else 0