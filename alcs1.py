t = int(input())
for  _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    prev = -10
    cur  = -1
    for i in range(n):
        if a[i]:
            if (i - prev) < 6:
                print('NO')
                break
            else:
                prev = i
    else:
        print('YES')



# 3 
# 3 
# 1 0 1
# 7 
# 1 0 0 0 0 0 1 
# 11 
# 0 1 0 0 0 0 0 1 0 0 1
