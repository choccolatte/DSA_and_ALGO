def binary_search(array, value)
	#establish lower and upper bounds of array. lower value will be first, upper will be last as its an ordered array
	lower = 0
	upper = array.length-1

	#a loop where we inspect middlemost value between lower and upper
	while lower <= upper do
		# we now find the midpoint btw the upper nad lower bounds
		midpoint = (upper + lower) / 2

		#inspecting midpoint's value
		midpoint_value = array[midpoint]

		#if value at midpoint is the target, we exit, else we change the lower and upper's value based on whether we need to guess higher or lower
		if value < midpoint_value
			upper = midpoint - 1
		elsif value > midpoint_value
			lower = midpoint + 1
		elsif value == midpoint_value
			return midpoint
		end
	end

	#if value not found in array, return nil
	return nil
end