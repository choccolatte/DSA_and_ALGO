import random as rd

arr = list(range(1, 101))
rd.shuffle(arr)

print('Unsorted array: ', arr)

# length of array
len_array=len(arr)

#looping through array - outer
for i in range(1, len_array):
    insert_index = i
    current_value = arr.pop(i)
        
    #looping through array - inner

    for j in range(i-1, -1, -1):
        if arr[j] > current_value:
            insert_index = j

    arr.insert(insert_index, current_value)
 
#printing sorted array
print('Sorted array: ', arr)