def solution(a, b, c, d):
    dice = [a, b, c, d]
    count_dict = {str(i): 0 for i in range(1, 7)}
    for num in dice:
        count_dict[str(num)] += 1
    
    for num_str, cnt in count_dict.items():
        if cnt == 4:
            return 1111 * int(num_str)
    
    counts = list(count_dict.values())
    if 3 in counts and 1 in counts:
        p = q = 0
        for num_str, cnt in count_dict.items():
            if cnt == 3:
                p = int(num_str)
            elif cnt == 1:
                q = int(num_str)
        return (10 * p + q) ** 2
    
    if counts.count(2) == 2:
        pairs = [int(num_str) for num_str, cnt in count_dict.items() if cnt == 2]
        return (pairs[0] + pairs[1]) * abs(pairs[0] - pairs[1])
    
    if 2 in counts:
        p = 0
        others = []
        for num_str, cnt in count_dict.items():
            if cnt == 2:
                p = int(num_str)
            elif cnt == 1:
                others.append(int(num_str))
        return others[0] * others[1]
    
    nums = [int(num_str) for num_str, cnt in count_dict.items() if cnt == 1]
    return min(nums)
