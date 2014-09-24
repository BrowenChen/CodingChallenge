# # Check if two strings are anagrams?
# Numbers Letters, Punct
# Case sensitive

# EX
# the eyes
# they see

# CASE sensitive
# punctuation

# A) all input is treated the same. Numbers, spaced, punctation. Therefore no particular character
	 # Same number of each character means base case, if len not equal. Not anagrams

	 # If same lengths, if same letters but case sensitive, it might fail
# D) Base case. Take both inputs, string1 and string2. If len != len return False

	# Iterate through string1, create a hash of inputs.
	# Increment the keys in the hash each time you see a character

	# On string2, you iterate through again, decrementing the hash. 
	# Then check values of the Hash. If they are all 0, then yes anagrams


# P)


# W)
# T) Test cases 


# Examplify
# Pattern Matching
# Base Case and Build
# Simplify and Generalize
# List Data Structures

def anagrams(string1, string2):

	str1 = string1
	str2 = string2

	if len(str1) != len(str2):
		return False 

	else:
		hashTab = {}
		# Starting the first loop
		for x in str1:
			
			if x not in hashTab.keys():
				
				hashTab[x] = 1
			elif x in hashTab.keys():
				hashTab[x] += 1
				
		# Starting the second loop
		for y in str2:
			if y not in hashTab.keys():
				return False
			elif y in hashTab.keys():
				hashTab[y] -= 1


		# Check if all are 0's
		for zero in hashTab.values():
			if zero != 0:
				return False

		#Pases everything return true!
		return True




# TEST CASES


print " TESTING "
print anagrams("the eyes","they see")
print anagrams("the eyes","they see!")
print anagrams("the eyes","they do see")
print anagrams("SCHOOL MASTER","THE CLASSROOM")
print anagrams("one sentence","a different sentence")




# Dijkstra's shortest path algorithm

# Similar to BFS. Start at a node and iterates through all the nodes to find the shortest path.  

# Graph class that can add nodes and edges with info for distances
class Graph:
	def __init__(self):
		self.nodes = set()
		self.edges = defaultdict(list)
		self.distances = {}


	def add_node(self, value):
		self.nodes.add(value)

	def add_edge(self, from, to, distance):
		self.edges[from].append(to)
		self.edges[to].append(from)
		self.distances[(from, to)] = distance





