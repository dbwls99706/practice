def slope(p1, p2):
    return (p2[1] - p1[1]) / (p2[0] - p1[0])

def solution(dots):
    pairs = [
        (dots[0], dots[1], dots[2], dots[3]),
        (dots[0], dots[2], dots[1], dots[3]),
        (dots[0], dots[3], dots[1], dots[2])
    ]
    for pair in pairs:
        if slope(pair[0], pair[1]) == slope(pair[2], pair[3]):
            return 1
    return 0