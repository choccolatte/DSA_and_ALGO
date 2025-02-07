import random as rd

unsorted_arr = list(range(1, 101))
rd.shuffle(unsorted_arr)

print('Unsorted array: ', unsorted_arr)

#function for counting sort
def countingSort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)

    while len(arr) > 0:
        num = arr.pop(0)
        count[num] += 1

    for i in range(len(count)):
        while count[i] > 0:
            arr.append(i)
            count[i] -= 1

    return arr

#using function on unsorted array
sorted_arr = countingSort(unsorted_arr)
print('Sorted array: ', sorted_arr)
