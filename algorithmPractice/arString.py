from collections import deque

# # Q1) Implement an algorithm to determine if a string has all unique characters

# 1) Resolve ambiguity
# 2) Design
# 3) PsuedoCode
# 4) Write
# 5) Test

# Five action methods

# 1) Examplify
# 2) Pattern Matching
# 3) Base Case and Build
# 4) Simplify and Generalize
# 5) Listing Data Structures

# Cases include: 1) all the same characters. 2) one different
# Therefore, all we do is keep a list of checked values and if it is contained in seen list, then we know this string isn't unique

# is this ASCII or Unicode string?
# Consider Space and Time Complexity, Data issues, 
# O(n) space because max is iterating through the string of length n once. 

#Option 2 is sorting in O(nlogn) time and compare neighbors
def uniChar(word):
	hasSeen = []
	for l in word:
		if l not in hasSeen:
			hasSeen.append(l)
		elif l in hasSeen:
			return False

	return True



# Q2) Reverse a string

# A) String of anything doesn't really matter, just Reverse
# D) -
# P) Create a second array, iterate backwards from the end of the string. Or use a stack and push to the front each iterate of the stirng. [asb]--> [bsa]
# W)  
# T) Edge cases include all characters the same? O(n) time. 

#This algorithm is pretty slow. Gotta make it more time efficient


def revString(word):

	stack = []
	result = []
	string = ''
	print len(word)
	for l in word: 
		print(l)
		stack.append(l)


	for s in range(len(stack)):
		
		result.append(stack.pop())

	
	for w in result:
		string += w

	return string








