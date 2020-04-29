n = int(input())
arr = list(map(int, input().split()))
srt = arr.copy()
srt = arr.sort()
mn1 = srt[0]
mn2 = srt[1]

idx1 = [i for i, v in enumerate(arr): if v == mn1]
idx2 = [i for i, v in enumerate(arr): if v == mn2]

for i in range(len(arr) - 1):
    for j in range(len(arr), i - 1, -1):
        if idx1 < i or idx1 > j:
            mn1 = mn2
            findmn1()
        if idx2 < i or idx2 > j:

