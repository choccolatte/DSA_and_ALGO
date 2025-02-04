import random as rd

arr = list(range(1, 1001))
rd.shuffle(arr)

print('Unsorted array: ', arr)

# length of array
no_arr = len(arr)

#loop through array
for i in range(no_arr-1):
    for j in range(no_arr-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
        
print('Sorted array: ', arr)