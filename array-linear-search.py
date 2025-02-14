import random as rd

arr = list(range(1, 10001))
rd.shuffle(arr)

print('Unsorted array: ', arr)

#deciding a target val - letting the user do it
targetVal = int(input('Enter target value to find (0-10000): '))

#defining linear search algo
def linearSearch(arr, targetVal):
    for i in range(len(arr)):
        if arr[i] == targetVal:
            return i
    return -1

#calling algo function
result = linearSearch(arr, targetVal)

if result != -1:
    print('User input', targetVal, 'found at:', result)
else:
    print('Value ', targetVal, 'not found')