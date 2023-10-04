"""
we want to convert an array into an increasing array, such that every element is at least as large as the previous element.
each time, we could add 1 to any of the element in the array.

so we iterating all elements from left to right, we use "step" to record how many times we need to add.
If current element smaller than the previous one, then step += arr[i]-arr[i-1];
also, we need to update the current element, such that arr[i]==arr[i-1]
"""

n = int(input())
arr = [int(ele) for ele in input().split()]
if len(arr)==1:
    step = 0
step = 0
for i in range(1,len(arr)):
    if arr[i]<arr[i-1]:
        step+=arr[i-1]-arr[i]
        arr[i]=arr[i-1]
print(step)