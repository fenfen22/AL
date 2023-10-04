n = int(input())
arr = [int(ele) for ele in input().split()]
res = (1+n)*n//2
for i in arr:
    res-=i
print(res)
