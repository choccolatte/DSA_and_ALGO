def linear_search(array, value)
	#iterate through every element in the array
	array.each do |element |

		#if value found, return it
		if element == value
			return value

		#if greater value found, exit earlu
		elsif element > value
			break
		end
	end

	#return nil if value not found within array
	return nil
end