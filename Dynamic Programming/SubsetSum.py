"""
Given n items from 1 to n;
Each item i has weight w_i;
There is a bound W;
Goal: select maximum weight subset S of items so that:
\sum_{i \in S} w_i \leq W  (sum of all weights in the subset is <= W)

For example:
Given 6 items: 2,5,8,9,12,18; and bound W = 25

the maximum weight subset S of items are 5,8,12, which is totally 25.


We start with the last element n to analysis the optimal solution.
For the OPT:
case1: OPT doesn't contain last element n, which is equal to optimal solution on using items {1,..,n-1} with capacity W
case2: OPT contains the last element n, which is equal to w_n + weight of optimal solution on {1,...,n-1} with capacity W-w_n

Recurrence:
OPT(i,w) = optimal solution on {1,..,i} with capacity w.
From above, we have:
OPT(n,W) = max(OPT(n-1,W), w_n+OPT(n-1,W-w_n))

IF w_n > W, we have: [we don't contain the element n in this case]
OPT(n,W) = OPT(n-1,W)


Totally:
OPT(i,w) = OPT(i-1, w)          if w < w_i
OPT(i,w) = max( OPT(i-1,w), w_i + OPT(i-1, w-w_i))

number os subproblems = nW;
COnstant time on each entry, so totally, we have O(nW)

This is pseudo-polynomial time (Not polynomial in input size)
We have nW entries totally, the whole input can be described as below:
n items, for each item, we use binay representation. so for each item, we need logn bits( we need logn bits to represent at most n). In order to represent n items, so totally we need nlogn bits to represent n items;
W is the maximum weight, we need logW bits to represent W.

Polynomial time means the time complexity is a function of input size.



"""
import numpy as np
# n is the number of items; W is the capacity bound
def initialM(n,W):
    M = [[False] * W for _ in range(n)]



def SubsetSum(i,w,M,Items):                        # top to bottom
    if M[i][w] == False and i-1 >=0:
        if w < Items[i-1]:                         # i-1: change the number to index
            M[i][w] = SubsetSum(i-1,w,M,Items)
        else:
            M[i][w] = max(SubsetSum(i-1,w,M,Items), Items[i-1]+SubsetSum(i-1,w-Items[i-1],M,Items))
    return M[i][w]

def bottom_up(n,W,M,Items):                           # bottom up
    for i in range(1,n+1):                            # from 1 to n, wo have n items totally
        for w in range(W+1):                          # capacity is from 0 to W
            if w < Items[i-1]:                        # if current weight large than the current capacity, we move to the next item, maximum weight is the same as the last one
                M[i][w] = M[i-1][w]
            else:
                M[i][w] = max(M[i-1][w], Items[i-1]+M[i-1][w-Items[i-1]])   #otherwise, we choose the maxmum between the last maximum weight, and current plus last suitable weight
    return M[n][W]



if __name__ == '__main__':
    # n = 6     # number of elements
    # W = 25    # bound
    # Items = [2,5,8,9,12,18]                                           # items should be sorted by increasing order

    n=5
    W = 12
    Items = [1,2,5,8,9]
    M = [[False] * (W+1) for _ in range(n+1)]                           # Initialize an array M[n+1][W+1]   n+1 rows and W+1 columns
    for j in range(W+1):
        M[0][j] = 0                                               # Initial the first row to 0, we didn't ass anything th the bag, so current weight is 0
    

    res = SubsetSum(n,W,M,Items)                                              # call this function to output the maximum weight
    # res= bottom_up(n,W,M,Items)
    print(res)



    for i in M:              # for printing the array M
        print(i)

