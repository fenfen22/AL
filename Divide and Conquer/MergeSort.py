# Merge Sort is a recursive algorithm that continuously splits the array in half until it can not be further splited
# i.e., the array has only one element left (an array with one element is always sorted). Then the sorted subarrays are merged into one sorted array

def MergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        Left = arr[:mid] # from the beginning to the element at the mid index (but not including)
        Right = arr[mid:]

        MergeSort(Left)
        MergeSort(Right)

        # Maintain current index of sub-arrays and main array; i for left; j for right; k for arr
        i = j = k = 0

        # Until we reach either end of either Left or Right, pick smaller among elements Left and Right
        # and place them in the correct position arr[k].
        while i < len(Left) and j < len(Right):
            if(Left[i] <= Right[j]):
                arr[k] = Left[i]
                i += 1
            else:
                arr[k] = Right[j]
                j += 1
            k += 1
        
        # If we run out of elements in either Left or Right, pick up the remaining elements in Left or Right
        # and put it in corresponding position arr[k].
        while i < len(Left):
            arr[k] = Left[i]
            k += 1
            i += 1
        
        while j < len(Right):
            arr[k] = Right[j]
            k += 1
            j += 1

def PrintArray(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print("\n")


if __name__ == '__main__':
    arr = [38,27,43,10]
    arr2 = [6,5,12,10,9,1]
    print("Given array is:")
    PrintArray(arr2)
    MergeSort(arr2)
    print("Sorted array is:")
    PrintArray(arr2)
