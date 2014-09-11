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



# Q3) Determine if one string is a permutation of another string

# A) Lenght of strings, what if one string is a subset of another string?
# D)
# P)
# w)
# T)

# 1) Examplify
# 2) Base Case and Expand
# 3) Generalize
# 4) Pattern Matching
# 5) Simplify and match

# How we can solve this problem: Hash table, go through all the letters of first string inserting 1 for each letter. Go through the second string
# and remove one from each hash. If all of the letters in the first hash of the second string is 0, then yes permutation

# Q4)

def permute(str1, str2):
	hash = {}

	for l in str1:
		if l not in hash:
			hash[l] = 1
		elif l in hash:
			hash[l]+= 1


	for w in str2:
		hash[w] -= 1

	# if all of the letters in str2 is 0 in the hash, then yes its a permutation
	print hash
	return 1


## Q5) Remove all spaces with %20 in a given string

# A) is there enough space at the end allocated for memory? Can we use additional data structures? 
# D) -
# P) Iterate once, mark all the spaces' indexs. Create a new array and reinsert. Everytime we hit an index that has a space, 
# add in %20 and subtract current index of original string by 2 because we added two additional things
# W) - 
# T) - 

def remSpace(word):
	marked = []
	newWord = ''
	curMarked = 0
	curIndex = 0

	for x in range(len(word)):
		if word[x] == ' ':
			marked.append(x)


	# Now that we got the indices of the spaces, while curIndex < len(word), we add in the original sentence
	# Everytime we hit an index, we add %20 and dont update the curIndex 



## Q6) Image represented by NxN matrix with each pixel 4 bytes. Method to rotate image by 90 degrees

# We will be shifting the index of the current column to the row. For example, (2, 3), where  2 is the x column will be switched
# to (3, 2)


# Matrix is list of tuples representing coordinates

# def rotateImg(matrix):



# Q7) Compression that counts repeated characters

# A) Numbers, Characters, 
# D) Last Character, curCount, Keep track in a list [a,3,b,3,...]
# P)
# W)
# T) Base cases is if no repeated characters. If there's only one character, how does it end

# How do you deal with the first number

def compression(word):
	lastChar = ''
	curCount = 1
	trackList = []

	newString = ''
	# Iterate to count the occurences the first time
	for x in range(len(word)):
		if word[x] != lastChar:
			if x != 0:
				trackList.append(lastChar)
				trackList.append(curCount)

			lastChar = word[x]
			curCount = 1



		elif word[x] == lastChar:
			curCount += 1




	# Function to get the last set
	trackList.append(lastChar)
	trackList.append(curCount)



	# Now we want to create a new string
	for x in range(len(trackList)):
		print trackList[x]
		# newString += trackList[x]

	# return newString
















	
	

