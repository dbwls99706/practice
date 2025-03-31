def solution(arr):
    cnt = 0
    while 1:
        pre_arr = arr.copy()
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] = arr[i]/2
            elif arr[i] < 50 and arr[i] % 2 == 1:
                arr[i] = arr[i]*2 + 1
            else:
                arr[i] = arr[i]
        if arr == pre_arr:
            return cnt
        cnt+=1