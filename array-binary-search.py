import random as rd
import timeit as tt

arr = list(range(1, 10001))
# rd.shuffle(arr)

print('Unsorted array: ', arr)

#deciding a target val - letting the user do it
targetVal = int(input('Enter target value to find (0-10000): '))

#defining linear search algo
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

result = binarySearch(arr, targetVal)
print(result)

# enter a sorting algo here to sort the unsorted array