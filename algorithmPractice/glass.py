 # Given a number n, return a number formed from the same digits of n that is
  # the number right before n. Example: Given 1342, you must return the number 1324.

 #  123 --> none
 #  213 -> 123

 #  12 -> none


 #  1234 -> none
 #  1324 -> 1234

 #  If all numbers are increasing in value, that's the lower limit
 #  Find the position where the number value decreases 
	# EX) in 1324 position 2 to 3 is place where you can swap

 # 1432 -> 1423

 # Iterate through the number digits, the last dip in value is where we will do the swap



def nextLowest(theNumber):
	lastNumber = 0
	curNumber = 1
	lastDip = 0

	string = str(theNumber)
	
	for i in range(len(string)):
		curNumber = string[i]
		if curNumber < lastNumber:
			lastDip = i

		else:
			lastNumber = curNumber

		print string[i]


# Repeated squaring method in python for RSA



import math 
def rsa(num):
	#Find the highest power of 2 that goes into num
	# return math.pow(num, 2	)
	exp = 0
	base = 2

	highestNum = 1
	highestExp = 0
	highest = False;

	while highest == False:
		exp += 1
		if math.pow(base, exp) > num:
			highest = True

		else:
			
			highestNum = math.pow(base, exp)


	return highestNum


def repeated_squaring(message, decrypt, modulo):
	curNum = decrypt
	binary = []

	while(curNum != 0):
		nextInt = rsa(curNum)
		binary.append(nextInt)
		curNum -= nextInt

	result = 1
	messageList = []


	mult = []

	for num in binary:
		print("printing in binary")
		print(num)
		leftOver = math.pow(message, num) % modulo
		print("left over is : ")
		print(leftOver)

		messageList.append(leftOver)



	for x in messageList:
		print("printing messageList ")
		print(x)
		result = result * x

	result = result % modulo
	


	return result





# Given a sorted array find the lowest sum that can't be made up from the numbers in O(n) time

# Can't be 1 or 3
# Cant be the sum of 1 or 3, which is 4
# 2 isn't targeted

# All the sums that include 1, all sums that include 3. 

# list of sums = []
# for each number in the array, add that number. 
# [1, 3]






# HACKERRANK

# The Utopian tree goes through 2 cycles of growth every year. The first growth cycle of the tree occurs during the monsoon, when it doubles in height. The second growth cycle of the tree occurs during the summer, when its height increases by 1 meter. 
# Now, a new Utopian tree sapling is planted at the onset of the monsoon. Its height is 1 meter. Can you find the height of the tree after N growth cycles?

# Input Format 
# The first line contains an integer, T, the number of test cases. 
# T lines follow. Each line contains an integer, N, that denotes the number of cycles for that test case.

# Constraints 
# 1 <= T <= 10 
# 0 <= N <= 60

# Output Format 
# For each test case, print the height of the Utopian tree after N cycles.


# GROWTH CYCLES  Monsoon and Summer 
# 1) Height x 2
# 2) Height + 1 meter


# TEST EDGE CASES


def findGrowth():
    numTests = input()
    curCycle = 1
    
    newTreeHeight = 1
    
    for x in range(int(numTests)):
        cycles = int(input())
        
        
        
        while (cycles > 0):
            if (cycles % 2 == 1):
                newTreeHeight = newTreeHeight * 2
                
            elif (cycles % 2 == 0):
                newTreeHeight += 1
            cycles -= 1
            
        print (newTreeHeight)
        newTreeHeight = 1
            
        
    
# findGrowth()




# A subsequence of a sequence is a sequence which is obtained by deleting zero or more elements from the sequence.
# You are given a sequence A in which every element is a pair of integers i.e A = [(a , w ), (a , w ),..., (a , w )].
# For a subseqence B = [(b , v ), (b , v ), ...., (b , v )] of the given sequence :
# We call it increasing if for every i (1 <= i < M ) , b < b .
# Weight(B) = v + v + ... + v .
# Task:
# Given a sequence, output the maximum weight formed by an increasing subsequence.
# Input:
# The first line of input contains a single integer T. T test-cases follow. The first line of each test-case contains an integer N. The
# next line contains a , a ,... , a separated by a single space. The next line contains w , w , ..., w separated by a single space.
# Output:
# For each test-case output a single integer: The maximum weight of increasing subsequences of the given sequence.
# Constraints:
# 1 <= T <= 5
# 1 <= N <= 150000
# 1 <= a <= 10 , where i ∈ [1..N]
# 1 <= w <= 10 , where i ∈ [1..N]


		


# A) Delete from the array if not increasing
#	Naive algorithm starts at every number and finds increasing lists
 	# Longest increasing 
 	# Edge Cases: Max sum requires less than max decreasing list?

#	Start from every number, find all greater numbers at that point. Recursively
#		all(num) + all(num[2])

# D)	Simplify: find all increasing subsequences, add all weight values and take the maximum



#	For numbers in list, keep track of the highest. Start at that number. 


# P)
#  iterate backwards, find the highest at number i
#   def highest()
#	for i in list

#		if len(list) == 0 || 1:
#			return list[i][1] The value of that number

#		list[i][1] Get the value of that number
#		if list[i] > list[i-1]:
#			return max(list[i][1] + highest[list[:i-1]])

#		elif list[i] <= list[i-1]:
#			return max(list[i][1] + highest[list[:i-2]])


# # W)
# # T)	





# def seqWeight():
#	cycles = input()


# Increasing Subsequences problem
# def nincr_seq_ivlad(seq):
#     dp = [1]*len(seq)
#     for i, ei in enumerate(seq):
#         for j in xrange(i):
#             if seq[j] < ei:
#                 dp[i] += dp[j]
#     return sum(dp)

# print nincr_seq_ivlad(range(10)), 2**10-1
# print nincr_seq_ivlad(range(20)), 2**20-1
# print nincr_seq_ivlad(range(9, -1, -1)), 10
# print nincr_seq_ivlad(range(19, -1, -1)), 20
# print nincr_seq_ivlad([1]*9), 9
# print nincr_seq_ivlad([-1]*19), 19

