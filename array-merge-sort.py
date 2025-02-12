import random as rd

unsortredarr = list(range(1, 101))
rd.shuffle(unsortredarr)

print('Unsorted array: ', unsortredarr)

#defining merge sort
def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid] 
    rightHalf = arr[mid:]

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge(leftHalf, rightHalf)

#defining merge function
def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

#printing sorted array
sortedArr = mergeSort(unsortredarr)
print('Sorted array: ', sortedArr)