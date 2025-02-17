def solution(ineq, eq, n, m):
    if eq == "=":
        return 1 if eval(f"n {ineq}{eq} m") else 0
    else:
        return 1 if eval(f"n {ineq} m") and n != m else 0
