
def getValue(a,b):
    max_val =max(a,b)

    outermost = max_val*(max_val-1)+1      # using math instead of arr
    # arr = [0 for _ in range(max(a,b))]
    # arr[0] = 1
    # for i in range(1,max(a,b)):
        # arr[i] = arr[i-1]+2*i
    # print(arr)
    if a==b:
        return outermost
    elif a>b:
        if a%2==0:
            return outermost+(a-b)
        elif a%2!=0:
            return outermost-(a-b)
    else:
        if b%2!=0:
            return outermost+(b-a)
        elif b%2==0:
            return outermost-(b-a)


n = int(input())
arrs = []
for _ in range(n):
    arr = [int(ele) for ele in input().split()]
    arrs.append(arr)


for i in arrs:
    a = i[0]
    b = i[1]
    print(getValue(a,b))
# getValue(8,9)


