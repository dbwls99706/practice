def solution(a, b, c):
    s1 = a + b + c
    s2 = a**2 + b**2 + c**2
    s3 = a**3 + b**3 + c**3

    if a == b == c:
        return s1 * s2 * s3
    elif a == b or b == c or a == c:
        return s1 * s2
    else:
        return s1
