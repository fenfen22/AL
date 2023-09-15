"""
how similar are ACAAFTC and CATGT?

align them such that:
1. all items occurs in at most one pair
2. no crossing pairs

Cost of alignment:
1. gap penalty
2. mismath cost for each pair of letters a(p,q)

Goal: find minimum cost alignment

Input to the problem: 2 trings X and Y, gap penalty p, and penalty matrix a(p,q)

For example:
A C A A G T C
- C A T G T -
      ^       1 mismatch, 2 gaps

A C A A - G T C
- C A - T G T -
              0 mismatch, 4 gaps

we consider the last character Xn in string X, and Ym in string Y.
In OPT either
1. Xn and Ym are aligned
          OPT = price of aligning Xn and Ym + minimum cost of alignning X(n-1) and Y(m-1)
2. Xn and Ym are not aligned
          either Xn and Ym (or both) is unaligned in OPT
          OPT = p + min(min cost of aligning X(n-1) and Ym, 
                        min cost of aligning Xn and Y(m-1))


we define SA(Xi, Yj) = min cost of aligning strings X[1..i] and Y[1..j]
case1: align Xi and Yj
    pay mismatch cost for Xi and Yj, + min cost of aligning X(i-1) and Y(j-1)
case2: leave Xi unaligned
    pay gap cost p + min cost of aligning X(i-1) and Yj
case3: leave Yj unaligned
    pay gap cost p + min cost of aligning Xi and Y(j-1)

Now, we could get the recurrence equations as below:
SA(Xi,Yj) = jp                     if i = 0 (pay gap cost p for all characters in Y)
SA(Xi,Yj) = ip                     if j = 0 (pay gap cost p for all characters in X)
SA(Xi,Yj) = min(
               (a(Xi,Yj) + SA(X(i-1),Y(j-1)),             for case 1
               p + SA(X(i-1),Yj)                          for case 2
               p + SA(Xi,Y(j-1))                          for case 3
                )
"""


def getPenalty(Pdict,A,c1,c2):
    return A[Pdict[c1]][Pdict[c2]]



"""
you should be very caution about the indexes in this part
"""
def SequenceAlignment(string1, string2, p, M, Pdict, A):     # M is a 2D array, with len(string2) rows, len(string1) columns
    for i in range(len(string1)+1):    # len(string2) = 0, we fill values in the firts row (represented by i), range is [0,len(string1)]
        M[0][i] = i*p
    for j in range(len(string2)+1):    # len(string1) = 0, we fill values in the firts column (represented by j), range is [0,len(string2)]
        M[j][0] = j*p
    for i in range(1, len(string1)+1):
        for j in range(1, len(string2)+1):    # we first fill each column
            case1 = getPenalty(Pdict,A,string1[i-1], string2[j-1]) + M[j-1][i-1]
            case3 = p+ M[j-1][i]
            case2 = p + M[j][i-1]
            M[j][i] = min(case1, case2, case3)
    return M[len(string2)][len(string1)]

# def getSolution(string1, string2,M,l1,l2, List):                                             # TODO I want to output our result after aligning two strings, but failed
#     # l1 = len(string1)      # index for column
#     # l2 = len(string2)      # index for row
#     # List = [[]]
#     List.append(M[l2][l1])
#     if l1==0 and l2==0:
#         return List
#     elif l1-1>=0 and l2-1>=0:
#         List.append(min(M[l2-1][l1], M[l2][l1-1], M[l2-1][l1-1]))
#         # List.append( min(getSolution(string1, string2, M, l1-1, l2,List), getSolution(string1, string2, M, l1, l2-1,List), getSolution(string1, string2, M, l1-1, l2-1, List) ))
#     return List



if __name__ == '__main__':
    string1 = "ACAAGTC"
    string2 = "CATGT"
    p = 1                                                    # gap cost
    A = [[0,1,2,2],[1,0,2,3],[2,2,0,1],[2,3,1,0]]            # initial the penalty matrix
    Pdict = {"A":0,"C":1,"G":2,"T":3}                        # dictionary for penalty matrix
    l1= len(string1)
    l2= len(string2)

    M = [[False] * (l1+1) for _ in range(l2+1)]              # initial memoization data structure

    res = SequenceAlignment(string1, string2, p, M, Pdict, A)
    # print(res)

    for i in M:                          # check M
        print(i)
    
    #print(getSolution(string1,string2, M, l1, l2,List))                   # TODO this function failed
  

