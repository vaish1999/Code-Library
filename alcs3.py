t = int(input())

for  _ in range(t):
    x, k = list(map(int, input().split()))
    cnt  = 0
    while not x % 2:
        x  //= 2
        cnt += 1

    for i in range(3, 1 + int((x ** 0.5) // 1), 2):
        while not x % i:
            x  //= i
            cnt += 1

    cnt += 1 if x >= 3 else 0

    print(0 if cnt < k else 1)