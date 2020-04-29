from bisect import bisect_left as lower_bound 
def getSum(BITree, index): 
  
    sum = 0 # Initialize result 
  
    # Traverse ancestors of BITree[index] 
    while (index > 0): 
  
        # Add current element of BITree to sum 
        sum += BITree[index] 
  
        # Move index to parent node in getSum View 
        index -= index & (-index) 
  
    return sum
  
# Updates a node in Binary Index Tree (BITree) at given index 
# in BITree. The given value 'val' is added to BITree[i] and 
# all of its ancestors in tree. 
def updateBIT(BITree, n, index, val): 
  
    # Traverse all ancestors and add 'val' 
    while (index <= n): 
  
        # Add 'val' to current node of BI Tree 
        BITree[index] += val 
  
    # Update index to that of parent in update View 
    index += index & (-index) 


def convert(arr, n): 

    temp = [0]*(n) 
    for i in range(n): 
        temp[i] = arr[i] 
    temp = sorted(temp) 
    for i in range(n): 
        arr[i] = lower_bound(temp, arr[i]) + 1


def getInvCount(arr, n): 

    invcount = 0 # Initialize result 
    convert(arr, n)

    BIT = [0] * (n + 1) 

    for i in range(n - 1, -1, -1): 
        invcount += getSum(BIT, arr[i] - 1) 

        print("SSSS", n)

        updateBIT(BIT, n, arr[i], 1) 

    return invcount 
if __name__ == '__main__': 

    arr = [8, 4, 2, 1] 
    n = len(arr) 
    print("Number of inversions are : ",getInvCount(arr, n)) 
