t = int(input())
for  _ in range(t):
    n    = int(input())
    if n == 1:
        print(1)
        print(1, 1)
    else:
        half = n // 2
        print(half)
        for i in range(0, half-1):
            t = i * 2
            print(2,t + 1,t + 2)
        if (n & 1):
            print(3,n-2,n-1,n)
        else:
            print(2,n-1,n)
