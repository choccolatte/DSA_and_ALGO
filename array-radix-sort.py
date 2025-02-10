import random as rd

arr = list(range(1, 1001))
rd.shuffle(arr)

print('Unsorted array: ', arr)

radixArray = [[], [], [], [], [], [], [], [], [], []]
maxVal = max(arr)
exp = 1

while maxVal // exp > 0:

    while len(arr) > 0:
        val = arr.pop()
        radixIndex = (val // exp) % 10
        radixArray[radixIndex].append(val)

    for bucket in radixArray:
        while len(bucket) > 0:
            val = bucket.pop()
            arr.append(val)

    exp *= 10

#printing sorted array
print('Sorted array: ', arr)