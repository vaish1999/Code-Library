t = int(input())
for  _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    p = sorted(p, reverse=True)
    profit = 0
    for y in range(n):
        if p[y] <= y:
            break
        profit += (p[y] - y)
        # profit += (p[y] - y) % 1_000_000_007
        # print(y, p[y], profit)
    print(profit % 1_000_000_007)

# 2 
# 3 
# 6 6 6 
# 3 
# 0 1 0