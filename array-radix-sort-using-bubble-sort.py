import random as rd

arr = list(range(1, 101))
rd.shuffle(arr)

print('Unsorted array: ', arr)

#defining bubble sort 
def bubbleSort(newArray):
    n = len(newArray)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# defining radix sort
def radixSortWithBubbleSort(newArray):
    maxVal = max(newArray)
    exp = 1

    while maxVal // exp > 0:
        radixArray = [[], [], [], [], [], [], [], [], [], []]

        for nums in newArray:
            radixIndex = (nums // exp) % 10
            radixArray[radixIndex].append(nums)

        for bucket in radixArray:
            bubbleSort(bucket)

        i = 0
        for bucket in radixArray:
            for nums in bucket:
                newArray[i] = nums
                i += 1

        exp *= 10

#printing sorted array
print('Sorted array: ', radixSortWithBubbleSort(arr))