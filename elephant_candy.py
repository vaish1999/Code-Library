t = int(input())
for i in range(t):
    n, c = list(map(int, input().split()))
    ak   = list(map(int, input().split()))
    sm = 0
    for s in ak:
        sm += s
    if sm <= c:
        print("Yes")
    else:
        print("No")