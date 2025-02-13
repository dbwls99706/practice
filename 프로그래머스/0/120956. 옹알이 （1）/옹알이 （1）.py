def solution(babbling):
    baby = ["aya", "ye", "woo", "ma"]
    answer = 0
    
    for i in babbling:
        for j in baby:
            i = i.replace(j, " ")
        if i.strip() == "":
            answer += 1
    
    return answer