import random as rd

my_arr = list(range(1, 1001))
rd.shuffle(my_arr)

# print (my_arr)

minVal=my_arr[0]

for i in my_arr:
    if i < minVal:
        minVal = i
    else:
        break

print('lowest value in array: ' , minVal)