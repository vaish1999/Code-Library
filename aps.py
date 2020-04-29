import itertools
n = 6


sum_array = []
for i in range(1, n+ 1 ):
    sum_array.append([])
    for num1 in range(1, i):
        for num2 in  range(1, i // 2 + 2):
            if num1 + num2 == i:
                sum_array[i - 1].append([num1, num2])
                sum_array[i - 1][-1].sort()
                # sum_array[i - 1] = set(sum_array[i - 1])
                if num2 > 1:
                    for ns in sum_array[num2 - 1]:
                        sum_array[i - 1].append([num1, *ns])
                        sum_array[i - 1][-1].sort()
                        # sum_array[i - 1].extend(sum_array[num2 - 1])
                if num1 > 1:
                    for ns in sum_array[num1 - 1]:
                        sum_array[i - 1].append([num2, *ns])
                        sum_array[i - 1][-1].sort()

    sum_array[i - 1] = list(x for x in {tuple(item) for item in sum_array[i - 1]})
    # sum_array[i - 1] = list(map(list, sum_array[i - 1]))

print((sum_array[5]))