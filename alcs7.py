def count(arr):
    n = len(arr)
    cnt = 0
    srt = -1
    end = 0
    t1  = 1
    t2  = 0
    oc = 0
    for nm in range(n):
        if not (arr[nm] & 1):
            cnt += ((oc ** 2) + oc) // 2
            oc   = 0
            if not (arr[nm] % 4):
                cnt += n - nm + n * nm - n * t2 - nm ** 2 + nm * t2
                t2 = nm + 1
                srt = -1
                t1 += 1
                end = 0
            else:
                srt = nm if srt == -1 else srt
                end = nm if end == 0 and nm > srt else end
                if end and srt >= 0:
                    cnt += n - end + n * srt - n * t2 - end * srt + end * t2
                    t2 = srt + 1
                    srt = end
                    end = 0
                    t1 += 1
        else:
            oc += 1
    return cnt + (((oc ** 2) + oc) // 2)


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(count(a))



# 2 
# 3 
# 1 2 3 
# 3 
# 2 5 6