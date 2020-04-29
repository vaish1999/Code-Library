cost = [[3, 2, 7],
        [5, 1, 3],
        [2, 7, 2]]
n     = 3
dp    = [float('inf') for i in range(2**n)]
dp[0] = 0


def count_set_bits(mask):
    cnt = 0
    while(mask != 0):
        cnt += 1
        mask &= (mask - 1)
    return cnt

print(count_set_bits(7)) 
# for mask in range(2**n):
#     x = count_set_bits(mask)