import random
t = int(input())
for _ in range(t):
    n, m, k = list(map(int, input().split()))
    out = []
    for _ in range(n):
        out.append(random.randint(1, m))
        arr = list(map(int, input().split()))
    print(*out)


# 1
# 3 4 2
# 1 2 
# 2 1
# 1 1 
# 2 2