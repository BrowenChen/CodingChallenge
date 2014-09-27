# ========================================
# PROBLEM
# The attached utf-8 encoded text file contains the favorite musical artists of 1000 users from LastFM. 
#Each line is a list of up to 50 artists, formatted as follows:

# Write a program that, using this file as input, produces a list of pairs of artists which appear TOGETHER in 
# at least fifty different lists. 
# ========================================






# ========================================
# MY SOLUTION AND WRITEUP
# Runtime of this algorithm depends on the split function, the number of lines in the text file, and the generatePairs function.

# The generatePairs function is a naive algorithm that generates all pairs in a given array. This is O(n^2) time, with n being the number
# of elements in that specific array. 

# This generatePairs function is run K times, with K being the number of lines in a given text file.

# Another for loop inside of the function goes through each pair of each line. There are N choose 2 pairs to iterate over for each line
# Ill call the number N choose 2 to be Y. Thus, the for loop will run K times, for the amount of lines in a given text file.__class__

# The swapTuple function just makes sure the tuple is in alphabetical order for the hash table
# Insertion and lookup for hashtables is fast, O(1) time. 

# So to put it all together, this algorithm runs in O(K * N^2 * Y) time, with K being the number of lines in the file, N being elements in 
# the longest line, and Y being the highest N choose 2 (for the number of pairings). 


# My current solution takes (textFile) a string input (the example given in the email), and checks for the artists that appear together more than 1 occurences

# To fit the original problem, I'd swap out the 1 to 50, and open the targeted text file (labled realFile)

# **********
# A problem with this code is there's something wrong with parsing the .txt files, something to do with the open() function and
# str.splitline() functions. That would be debugging issues, but the algorithm works if the data is in string format. 
# ========================================

def similarArtists(testInputFile):
 
	textFile = convertTextFile(testInputFile) #Demo example. This script uses this one <<<<<<

	realFile = split() #Takes in the real txt file. 

	pairCount = {} #Hash table. Keys are the pairs and values are the # of occurences
	output = [] #The aritists meeitng the qualifications

	#We seperate the text file by new line \n
	for line in textFile:
		#Generate list of pairs (artist, anotherArtist)
		artistList = line.split(',')

		pairs = generatePairs(artistList)

		#Iterate through the pairs, if the pair is not in the keys of the hash, add it.
		for pair in pairs:

			#This is to remove duplicates. Sort key tuples by alphabetical
			keyPair = swapTuple(pair)

			if keyPair not in pairCount.keys():
				pairCount[keyPair] = 1

			else:
				pairCount[keyPair] += 1

	#After counting for the pairs, find the keys with values > 50
	# print pairCount
	for item in pairCount.keys():
		# print pairCount[item]
		if pairCount[item] >= 2:
			# bob = 0
			output.append(item)

	return output
	# print output


def generatePairs(line):
	#generates the list of all possible pairings in the given line
	output = []
	for x in range(len(line)):
		j = x + 1
		while j < len(line):
			output.append((line[x], line[j]))
			j += 1


	return output


#Sort the tuple to be alphabetical for keys
def swapTuple(pairing):
	firstPairLetter = pairing[0][0]
	secondPairLetter = pairing[1][0]

	if firstPairLetter < secondPairLetter:
		return pairing
	else:
		return (pairing[1], pairing[0])

#Parse the input text file into arrays of lines. Each artist is seperated by a colon. Uses example data
def convertTextFile(textInput):
	outputFile = []

	# data = textFile.read() #Turning it into a string
	outputFile = textInput.splitlines()
	return outputFile

#This uses the real txt file
def split():
	f1 = open("Artist_lists_small.txt", "r")
	data = f1.read()
	output = data.split("\n")

	return output



# TESTING SECTION

testList = ["joe", "bob", "robert", "lee"]
secondList = ["joe", "bob", "owen", "marcus"]
thirdList = ["joe", "bob", "robert", "naruto"]

testInputFile = [testList, secondList, thirdList]

#The test data in the email
testData = "Radiohead,Pulp,Morrissey,Delays,Stereophonics,Blur,Suede,Sleeper,The La's,Super Furry Animals\n Band of Horses,Iggy Pop,The Velvet Underground,Radiohead,The Decemberists,Morrissey,Television\n"



print "Using test data, x = 1"
print "Artists in that appear above x times in lists are: \n "
print similarArtists(testData)


print "Algorithm description in the comments at the top of the .py file  \n"








