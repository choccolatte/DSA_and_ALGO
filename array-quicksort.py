import random as rd

# partition function
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range (low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

# quicksort function
def quicksort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index-1)
        quicksort(arr, pivot_index+1, high)


#getting random array
unsorted_arr = list(range(1, 101))
rd.shuffle(unsorted_arr)

print('Unsorted array: ', unsorted_arr)

#printing the sorted array
quicksort(unsorted_arr)
print('Sorted array: ', unsorted_arr)