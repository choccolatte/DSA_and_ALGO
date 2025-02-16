import random as rd

arr = list(range(1, 101))
rd.shuffle(arr)

print('Unsorted array: ', arr)

#deciding a target val - letting the user do it
targetVal = int(input('Enter target value to find (0-100): '))

#defining binary search algo
def binarySearch(arr, targetVal):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == targetVal:
            return mid

        if arr[mid] < targetVal:
            left = mid + 1

        else:
            right = mid -1

    return -1


# adding a sorting algo here to sort the unsorted array
# length of array
len_array=len(arr)

#looping through array - outer
for i in range(len_array):
    min_index = i
    
    #looping through array - inner

    for j in range(i+1, len_array):
        if arr[j] < arr[min_index]:
            min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]
 
#printing sorted array
print('Sorted array: ', arr)

result = binarySearch(arr, targetVal)
print(result)
