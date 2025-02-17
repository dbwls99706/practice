def solution(num_list):
    n1 = 1
    n2 = 0
    for i in num_list:
        n1 *= i
        n2 += i
    return int(n1 < n2**2)