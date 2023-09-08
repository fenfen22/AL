"""
Weighted interval scheduling problem
Job j starts at sj, finishes at fj, and has weight or value vj.
Two jobs are compatible if they do not overlap. 
Goal: find maximun weight subset of mutually compatible(non-overlapping) jobs.


First: label/sort jobs by finishing time: f1 <= f2 <= f3 <= f4 <=...<= fn
P[j], which is the largest index i < j such that job i is compatible with j

optimal solution OPT:
case1: OPT select the last job;
        OPT = vn + optimal solution to subproblem on 1,...,P[n]
case2: OPT does not select the last job
        OPT = optimal solution to subproblem on 1,..,n-1

Therefore, we get a recursion as below:
OPT(j) = 0, if j = 0;
OPT(j) = max(vj+OPT(P[j]),OPT[j-1])

"""

class Job:
    # for each job, it has start time(st), finish time(ft) and profit(pro)
    def __init__(self, st, ft, pro):       
        self.st = st
        self.ft = ft
        self.pro = pro

# this function is helpful for sorting jobs by finish time
def jobComparator(j):
    return j.ft

# according to this function to calculate p[i] based on a finish time array and job i
def latesNonConflict(arr, i):
    for j in range(i-1, -1, -1):            # p[i] < i
        if arr[j].ft <= arr[i].st:          # finish time of j smaller than start time of i, which means they are mutually compatible
            return j
    return -1

"""
brute force

based on the equations:
OPT(j) = 0; if j = 0
OPT(max(pro_j + OPT(p[j]), OPT(j-1))), otherwise

which mean the current last job j either in the OPT solution or not in the OPT solution.
if job j is in the OPT solution, then we recursively check job that are not overlap (p[j] now is the current last job) with job j
if job j is not in the OPT solution, then we recursively check other jobs except job j (now job j-1 is the current last job)

Time complexity is O(2^n), not polynomial time.
"""
def computeBruteForceOpt(arr,j,p):
    # j == 0 is base case, which means there is only 1 job in the job list
    if j == 0:
        return arr[j].pro
    else:
        incluPro = arr[j].pro
        if p[j] != -1:          # if p[j]!= -1, means we could get find a p[j]
            incluPro += computeBruteForceOpt(arr, p[j], p)              # the profit contains the current job
        excluPro = computeBruteForceOpt(arr, j-1, p)                                # the profit doesn't contain the current job
        return max(incluPro, excluPro)                                              # we choose the larger one


"""
weighted interval scheduling memoization:
we use a list M[] to store the result of each subproblem. For each subproblem, we only solve once.
Time complexity is O(nlogn); space complexity is O(n)
"""
def computeMemoizedOPT(arr,j,p,M):
    # j == 0 is base case, which means there is only 1 job in the job list
    if j == 0:
        M[j] = arr[j].pro

    # if M[j] is empty, whcih mean we didn't calculat M[j] before, so we calculate this value and store it
    # so for each current last job, we only calculate once
    # if M[j] is not empty, we just return its value
    elif M[j] == -1:
        incluPro = arr[j].pro                                   # the profit contains the current job
        if p[j]!= -1:
            incluPro += computeMemoizedOPT(arr, p[j], p, M)
        excluPro = computeMemoizedOPT(arr, j-1, p, M)           # the profit doesn't contain the current job
        M[j] = max(incluPro, excluPro)
    return M[j]

"""
after all job are sorted by finish time;
we start from the first job to the last job
since we already sorted the jobs and calculated the p[], so in this function, the time complexity is O(n) for the loop

space complexity is O(n)
"""
def bottom_up(arr, j ,p ,M):
    M[0] = arr[0].pro

    for i in range(1,j+1):
        incluPro = arr[i].pro                                   # the profit contains the current job
        if p[i]!= -1:           # could find a p[i]
            incluPro += bottom_up(arr, p[i], p, M)
        excluPro = bottom_up(arr, i-1, p, M)           # the profit doesn't contain the current job
        M[i] = max(incluPro, excluPro)
    return M[j]

"""
we want to know which jobs give us the max profits.
"""
def findJobsUlti(j,p,M):    # j is the index of the last job
    result = []
    if j == -1:             # which means the job list is empty
        return False

    elif M[j]>M[j-1]:       # current job is one of jobs give the max profits
        result.append(j)
        result.append(findJobsUlti(p[j],p,M))
        return result                           # we get a nested list
    else:
        return findJobsUlti(j-1,p,M)        # current job is not one of jobs give the max profits

def findJobs(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(findJobs(item))
        elif item is not False:
            result.append(item)
    return result




if __name__ == '__main__':
                   
    List = [[0,6,2],[1,4,4],[1,3,1],[3,8,9],[4,7,7],[5,9,5],[6,10,6],[8,11,4]]  # the index of each job in the list starts at 0
    n = len(List)                                                               # number of jobs, starts at 1

    # initial job class
    arr = []
    for i in List:
        arr.append(Job(i[0],i[1],i[2]))
    
    arr.sort(key=jobComparator)                     # sort the job arr by finish time, so arr now is sorted by finish time

    # compute the largest job index i that are not overlap with job j for reach job j
    p = [-1]*n
    for i in range(n-1,-1,-1):
        p[i] = latesNonConflict(arr, i)
    
    
    # check the brute force
    print("result_brute_force_OPT:", computeBruteForceOpt(arr,n-1,p))             # start from the last job, whose index is n-1

    M = [-1]*n          # initial M
    print("result_memoized_OPT:", computeMemoizedOPT(arr,n-1, p, M))              # calculate M 
    
    print("result:", bottom_up(arr,n-1, p, M))                                    # calculate M
   
    result = findJobsUlti(n-1,p,M)                                                # u need calulate M before call findJobsUlti function
    print("List:", findJobs(result))




    
    
