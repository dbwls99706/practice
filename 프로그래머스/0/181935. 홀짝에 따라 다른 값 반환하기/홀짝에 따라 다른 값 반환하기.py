def solution(n):
    return sum(i if n % 2 else i**2 for i in range(1 if n % 2 else 2, n + 1, 2))

