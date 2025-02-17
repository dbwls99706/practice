def solution(num_list):
    r = num_list[-1] - num_list[-2]
    if r > 0:
        num_list.append(r)
    else:
        num_list.append(num_list[-1] * 2)
    return num_list