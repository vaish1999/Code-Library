import itertools
from itertools import chain
from collections import Counter

budget = 6

pool = [2, 4, 5, 1]

org_pool = pool.copy()

pool.append(budget)

pool.sort()
# print(pool)


sum_array = []
for i in range(pool[-1] + 1):
    # print(i)
    sum_array.append([])

for i in pool:
    for num1 in pool:
        for num2 in  pool:
            if num1 + num2 == i:
                # print(i)
                sum_array[i].append([num1, num2])
                sum_array[i][-1].sort()
                # sum_array[i - 1] = set(sum_array[i - 1])
                # if num2 > 1:
                for ns in sum_array[num2]:
                        sum_array[i].append([num1, *ns])
                        sum_array[i][-1].sort()
                        # sum_array[i - 1].extend(sum_array[num2 - 1])
                # if num1 > 1:
                for ns in sum_array[num1]:
                        sum_array[i].append([num2, *ns])
                        sum_array[i][-1].sort()

    sum_array[i] = list(x for x in {tuple(item) for item in sum_array[i]})
    # sum_array[i - 1] = list(map(list, sum_array[i - 1]))


freq = {}
for ele in org_pool:
    freq[ele] = org_pool.count(ele)

print((sum_array[budget]))
print(org_pool)
print(freq)


total = 0

# t_cities = 3

for comb in sum_array[budget]:
    # if len(comb) > t_cities:
    #     sum_array.remove(comb)
    #     continue

    flag = 0
    for x in comb:
        if comb.count(x) > freq[x]:
            flag = 1
            break
    if flag == 0:
        total += 1
        print(comb)

print(total)