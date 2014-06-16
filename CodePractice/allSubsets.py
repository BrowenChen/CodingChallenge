"""
Write a method that returns all subsets of a subsets
allSubsets.py

>>> subsets([1, 2, 3])
> [1], [2], [3], [1,2] [1,3], [2,3], [1,2,3]

"""



def subsets(list):
	#Base case, if list.len == 1
	print("Current List")
	print(list)

	if (len(list) == 1):
		return list
	else:
		print(list[:1])

		newSub = list[1:]
		print(newSub)		
		return list[:1] + subsets(newSub), list[:1]
ans = subsets([1,2,3])
print(ans)

	#Return list[1] + subsets[1:], list[1]