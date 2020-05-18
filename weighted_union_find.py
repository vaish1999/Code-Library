def root(arr, idx):
    while(arr[idx] != idx):
        idx = arr[idx]
    return idx


def union(arr, size, u, v):
    rootu = root(arr, u)
    rootv = root(arr, v)
    if size[rootu] > size[rootv]:
        arr[rootv] = arr[rootu]
        size[rootu] += size[rootv]

    else:
        arr[rootu] = arr[rootv]
        size[rootv] += size[rootu]

    return arr, size


if __name__ == '__main__':
    arr = [0, 1, 2, 3, 4, 5]
    size = [1 for i in range(6)]

    arr, size = union(arr, size, 0, 1)
    print(arr, size)
    arr, size = union(arr, size, 1, 2)
    print(arr, size)
    arr, size = union(arr, size, 2, 3)
    print(arr, size)
