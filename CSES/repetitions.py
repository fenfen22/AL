"""
iterating the elements from left to right, keeping track the current repetition and the longest repetition so far.
"""

s = input()

cur_rep = s[0]
cur_cou = 1
max_rep =None
max_cou = 0

for i in range(1,len(s)):
    if s[i]==cur_rep:
        cur_cou+=1
    else:
        if cur_cou >max_cou:
            max_rep = cur_rep
            max_cou = cur_cou
        cur_rep = s[i]
        cur_cou = 1

if cur_cou>max_cou:
    max_rep= cur_rep
    max_cou=cur_cou
print(max_cou)
