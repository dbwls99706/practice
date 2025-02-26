def solution(my_string, is_prefix):
    pref = []
    for i in range(len(my_string)):
        pref.append(my_string[:i])
    return 1 if is_prefix in pref else 0