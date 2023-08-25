"""
Binary search works on Sorted Array.

Binary search begins by comparing an element in the middle of the array with the target value.
If the target value matches the element, its position in the array is returned;
if the target value is less than the element, the search continues in the lower half of the array;
otherwise, the search continues in the upper half of the array.

By doing this, the algorithm eliminates the half in which the target value cannot lie in each iteration.

Time complexity is O(logn), because in the worst case, making O(logn) comparison, where n is the number 
of elements in the array.

"""

# this algorithm checks whether arr[mid] is equal to tar in every iteration
def BinarySearch(arr, tar):
    left, right = 0, len(arr)-1
    while(left <= right):
        mid = left + ((right-left)//2)

        if( tar < arr[mid]):
            right = mid - 1
        elif( tar > arr[mid]):
            left = mid + 1
        else:
            return mid
    return -1   # return -1 means failed in this code

# this algorithm performs this check only when one element is left(left == right), which results a faster comparison loop
def BinarySearchAlternative(arr, tar):
    left, right = 0, len(arr)-1
    while(left != right):
        mid = left + ((right-left)//2)
        if tar < arr[mid]:
            right = mid -1
        else:
            left = mid
    if arr[left] == tar:
        return left
    return -1  # return -1 means failed in this code

# procedure for finding the leftmost element in a arr with duplicate elements
def BinarySearchLeftmost(arr, tar):
    left, right = 0, len(arr)-1
    # leftmost = -2   # flag for checking if we find the tar or not
    while left < right:
        mid = left + ((right-left)//2)
        if tar > arr[mid]:
            left = mid + 1
        else:
            right = mid
    return left


# procedure for finding the righmost element in a arr with duplicate elements
def BinarySearchRightmost(arr, tar):
    left, right = 0, len(arr)-1
    while left < right:
        mid = left + ((right-left)//2)
        if tar < arr[mid]:
            right = mid
        else:
            left = mid+1
    return left -1


if __name__ == '__main__':
    arr1 = [1,2,3,4,5,6,7,8,9]
    tar1 = 7
    # print(BinarySearch(arr1,tar1))

    arr2 = [1,2,5,8,8,8,12,13,18,20,25]
    tar2 = 8
    print(BinarySearchLeftmost(arr2, tar2))
    print(BinarySearchRightmost(arr2, tar2))