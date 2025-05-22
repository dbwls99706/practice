import math
def solution(n):
    a = math.sqrt(n)
    if a == int(a):
        return (a+1)**2
    else:
        return -1