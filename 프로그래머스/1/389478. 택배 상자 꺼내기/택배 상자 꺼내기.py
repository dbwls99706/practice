def solution(n, w, num):
    target = (num - 1) // w
    total = (n - 1) // w

    answer = total - target

    r = n % w if n % w != 0 else w

    num_col = (num - 1) % w
    top_col = (n - 1) % w

    if target % 2 == total % 2:
        if num_col <= top_col:
            answer += 1
    else:
        if num_col + r >= w:
            answer += 1

    return answer