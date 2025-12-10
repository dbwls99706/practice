T = int(input())
for _ in range(T):
    n = int(input())
    k1 = input().split()
    k2 = input().split()
    c  = input().split()

    pos = {w:i for i,w in enumerate(k1)}

    plain = [None] * n
    for i in range(n):
        plain[pos[k2[i]]] = c[i]

    print(*plain)
