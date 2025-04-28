function selectionSort(array){
	for (var i = 0; i < array.length; i++)
	{
		var lowerstNumIndex = i
		
		for (var j = i + 1; j <=array.length; j++)
		{
			if (array[j] < array[lowerstNumIndex])
			{
				lowerstNumIndex = j
			}
		}

		if(lowerstNumIndex != i)
		{
			var temp = array[i]
			array[i] = array[lowerstNumIndex]
			array[lowerstNumIndex] = temp
		}
	}
	return array
}