def solution(n, k):
    return [k*(i+1) for i in range(n//k)]