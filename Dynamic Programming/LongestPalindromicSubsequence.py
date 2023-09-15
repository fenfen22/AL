"""
For a given string, we want to find the length of the longest palindromic subsequence in it.

The longest palindromic subsequence (LPS) is the problem of finding a maximum-length subsequence of a given string that is also a Palindrome

case1: every single character is a palindrome of length 1
      L(i,i) = 1 for all indexes i in given sequence
case2: if frist and last characters are not same
      if(x[i]!=x[j])   L(i,j) = max( L(i+1,j), L(i,j-1) )
case3: if there are only 2 characters and both are same
      else if(j==i+1)       L(i,j) = 2
case4: if there are more than 2 characters, and first and last characters are same
      else L(i,j) = L(i+1,j-1)+2
"""

def LPS(seq, i,j):
    # base case, if there is only one character, return 1
    if i == j:
        return 1
    # if there are only 2 character and both are same, return 2
    if j==i+1 and seq[i]==seq[j]:
        return 2
    if seq[i]!=seq[j]:
        return max(LPS(seq, i+1,j), LPS(seq,i,j-1))
    else:
        return LPS(seq, i+1,j-1)+2

if __name__ == '__main__':
    seq = "bcadfbbba"
    print(LPS(seq,0,len(seq)-1))