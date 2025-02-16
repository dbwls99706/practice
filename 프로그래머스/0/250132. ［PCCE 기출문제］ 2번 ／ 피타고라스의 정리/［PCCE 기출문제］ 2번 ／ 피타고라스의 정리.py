a = int(input())
c = int(input())

b_square = sum(c for _ in range(c)) - sum(a for _ in range(a))
print(b_square)