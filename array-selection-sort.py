import random as rd

arr = list(range(1, 101))
rd.shuffle(arr)

print('Unsorted array: ', arr)

# length of array
len_array=len(arr)

#looping through array - outer
for i in range(len_array-1):
    min_index = i
    
    #looping through array - inner

    for j in range(i+1, len_array):
        if arr[j] < arr[min_index]:
            min_index = j
    
    min_value = arr.pop(min_index)
    arr.insert(i, min_value)

#printing sorted array
print('Sorted array: ', arr)