def solution(arr, queries):
    answer = []
    for query in queries:
        a = [arr[i] for i in range(query[0], query[1]+1) if arr[i] > query[2]]
        if a:
            answer.append(min(a))
        else:
            answer.append(-1)
    
    return answer
