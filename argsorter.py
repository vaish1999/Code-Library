def argsort(lst):
    idx = [i for i in range(len(lst))]
    zp  = list(zip(lst, idx))
    zp.sort()
    return list(zip(*zp))[1]

if __name__ == '__main__':
    import random
    n = int(input())
    a = [random.randint(0, 10) for i in range(n)]
    print(a)
    print(argsort(a))
    print(1232)