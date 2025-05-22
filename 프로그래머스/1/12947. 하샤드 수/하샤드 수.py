def solution(x):
    h = 0
    for i in str(x):
        h += int(i)
    return x % h == 0