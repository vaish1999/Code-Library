t = int(input())
mv = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
price = [25, 50, 75, 100]
total = 0

comb = []

idx1 = [0, 1, 2, 3]
for i1 in idx1:
    idx2 = [0, 1, 2, 3]
    idx2.remove(i1)
    for i2 in idx2:
        idx3 = [0, 1, 2, 3]
        idx3.remove(i1)
        idx3.remove(i2)
        for i3 in idx3:
            idx4 = [0, 1, 2, 3]
            idx4.remove(i1)
            idx4.remove(i2)
            idx4.remove(i3)
            for i4 in idx4:
                comb.append([i1, i2, i3, i4])
# print(comb)
# print(len(comb))
for case in range(t):
    table = [[0 for i in range(4)] for j in range(4)]
    n = int(input())
    for N in range(n):
        movie, time = input().split()
        time = (int(time) // 3) - 1
        movie = mv[movie] 
        table[movie][time] += 1

    profit_arr = []
    mx = -float('inf')
    for c in comb:
        p_arr = []
        for ix, v in enumerate(c):
            p_arr.append(table[ix][v])
        p_arr.sort()
        s = 0
        for ij, p in enumerate(p_arr):
            s += p * price[ij] if p > 0 else -100
        if s > mx:
            mx = s
            profit = s
        # print(p_arr)

    # for i in range(len(profit_arr), 4):
    #     profit_arr.append(0)

    # profit_arr.sort()


    # profit = 0
    # for ij, p in enumerate(profit_arr):
    #     profit += p * price[ij] if p > 0 else -100
    # # print("profit_arr:", profit_arr)
    total += profit
    # print("case:", case)
    # print("profit:", profit)
    print(profit)
print(total)


