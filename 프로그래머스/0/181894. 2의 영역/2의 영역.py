def solution(arr):
    answer = []
    r = []
    for i in range(len(arr)):
        if arr[i]==2:
            r.append(i)
    if len(r)>1:
        return arr[r[0]:r[-1]+1]
    elif len(r)==1:
        return [arr[r[0]]]
    else:
        return [-1]