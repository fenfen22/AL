"""
Given n items {1,...,n};
Item i has weight w_i and value v_i;
Bound W;
Goal: select maximum value subset S of items so that:
\sum_{i \in S} w_i \leq W  (sum of all weights in the subset is <= W)

For example:
capacity 12;
(value,weight): (1,2),(6,3),(18,5),(22,6),(28,9)
OPT: (18,5),(22,6)---> total weight is 11 <=12; total value is 40

Running time O(nW) np problem
"""

"""
First formulate the problem recursively:
1. describe the problem recursively in a clear and precise way
2. give a recursve formula for the problem

OPT(i,w) = OPT(i-1, w)          if w < w_i
OPT(i,w) = max( OPT(i-1,w), w_i + OPT(i-1, w-w_i))
------------------------------------------------------------------------------------
"""
class Items:
    def __init__(self, listItem):
        self.val = listItem[0]
        self.wei = listItem[1]

"""
Bottom-up:
1. identify all the subproblems
2. choose a memoization data structure
3. identify dependencies
4. Find a good evaluation order
"""
def bottom_up(M,n,W,arr):
    for i in range(1,n+1):
        for w in range(W+1):
            if w < arr[i-1].wei:
                M[i][w] = M[i-1][w]
            else:
                M[i][w] = max(M[i-1][w], arr[i-1].wei + M[i-1][w-arr[i-1].wei])
    return M[i][w]  
"""
Top-down:
1. identify all the subproblems
2. choose a memoization data structure
3. identify base cases.
4. remember to save results and check before computing
"""
def top_bottom(M,n,W,arr):
    if M[n][W] == False:                                       # if this position is empty, we recusively call this function to get the value of this position
        if arr[n-1].wei < W:
            M[n][W] = top_bottom(M,n-1,W,arr)
        else:
            M[n][W] = max(top_bottom(M,n-1,W,arr), arr[n-1].wei + top_bottom(M,n-1,W-arr[n-1].wei,arr))
    return M[n][W]

if __name__ == '__main__':
    List = [[1,2],[6,3],[18,5],[22,6],[28,9]]
    W = 12
    n = len(List)
    arr = []

    for i in List:
        arr.append(Items(i))
    
    M = [[False] * (W+1) for _ in range(n+1)]                           # Initialize an array M[n+1][W+1]   n+1 rows and W+1 columns
    for j in range(W+1):
        M[0][j] = 0  
    
    res1 = bottom_up(M,n,W,arr)                                          # call bottom up function
    res2 = top_bottom(M,n,W,arr)
    print(res2)
    
    # print(arr)
    # print(arr[1].val)

