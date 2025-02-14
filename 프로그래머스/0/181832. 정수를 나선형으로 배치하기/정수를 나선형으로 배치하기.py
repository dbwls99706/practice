def solution(n):
    a = [[0]*n for _ in range(n)];
    i = j = 0 
    di, dj = 0, 1
    for k in range(1,n*n+1):
        a[i][j] = k
        if not(0 <= i + di < n and 0 <= j + dj < n and not a[i + di][j + dj]): 
            di, dj = dj, -di
        i,j = i + di, j + dj
    return a