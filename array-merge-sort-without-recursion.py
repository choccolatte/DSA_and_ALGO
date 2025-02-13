import random as rd

unsortredarr = list(range(1, 1001))
rd.shuffle(unsortredarr)

print('Unsorted array: ', unsortredarr)

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

#defining merge sort
def mergeSort(arr):

    step = 1 # starting with sub-array of length 1
    length = len(arr)

    while step < length:
        for i in range(0, length, 2 * step):
            left = arr[i:i+step]
            right = arr[i+step:i+2*step]

            merged = merge(left, right)

            #place the merged array back into the original array
            for j, val in enumerate(merged):
                arr[i+j] = val

        step *= 2 # double the sub-array length for the next iteration

    return arr

#printing sorted array
sortedArr = mergeSort(unsortredarr)
print('Sorted array: ', sortedArr)