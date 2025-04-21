import random as rd

lst = list(range(1, 1001))
rd.shuffle(lst)

def bubble_sort(list):
	unsorted_until_index = len(list) -1
	sorted = False

	# loop through array
	while not sorted:
		#base case
		sorted = True

		#for loop to sort the range
		for i in range(unsorted_until_index):

			# if condition to check whether n and n+1 are sorted or not`
			if list[i] > list[i+1]:
				sorted = False
				list[i], list[i+1] = list[i+1], list[i]

		unsorted_until_index -= 1

bubble_sort(lst)
print (lst)