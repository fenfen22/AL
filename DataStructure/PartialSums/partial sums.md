### Partial Sums
Maintain array A[0,1,...,n] of integers support the following operations.
* Sum(i): return A[1]+A[2]+...+A[i]
* update(i,deta): set A[i] = A[i] + deta

#### solution 1: Explicit Array (Maintain A explicitly)
slow sum and super fast update.
* sum(i) : compute A[0]+...+A[i]
* udpdate(i,deta): set A[i] = A[i] + deta
Time:
sum O(n)
update O(1)

#### solution 2: Explicit partial sum (Maintain partial sum P of A)
super fast sum and slow update.
* sum(i): return P[i]
* update(i,deta): add deta to P[i], P[i+1],...,P[n]
Time
sum O(1)
update O(n)


#### solution 3: Balanced Binary tree
fast sum and dast update.
Maintain balanced binary tree T on A. Each node stores the sum of elements in subtree.
* sum(i): traverse path to i+1 and sum up all off-path nodes
* update(i,deta): add deta to nodes on path to i

Time
sum O(log n) ----> the height of this tree
update O(log n) ----> height of this tree


#### solution 4: Fenwick Tree
replace array A by another array F.
* replace all **even** entries A[2i] by A[2i-1]+A[2i]
* recurse on the entriex A[2,4,..,n] until we are left with single element.
Space: in-place. (No extra space)

* sum(i): add largest partial sums covering [1,...,i]
* indexes i_0, i_1, .. in F given by i_0 = i, and i_(j+1) = i_j -rmb(i_j). rmb(i_j) is the integer corresponding to the rightmost 1-bit in i. Stop when we get 0
* time is O(log n)

* update(i, deta): add deta to partial sums covering i.
* indexes i_0, i_1,.. in F given by i_0 = i and i_(j+1) = i_j + rmb(i_j). Stop when we get 0
* time is O(log n)