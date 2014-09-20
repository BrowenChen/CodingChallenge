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



		