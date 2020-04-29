def bc(n, k):
    if not k or k == n:
        return 1
    return bc(n-1, k-1) + bc(n-1, k)

if __name__ == '__main__':
    print(bc(5, 0))