import math
import heapq
# Summing the N Series
# You are given a series, whose n term is defined as
# T = n^2 - (n-1)^2
# You have to find the Sum of the series S = T + T + T + .... + T
# Find S % (10^9 + 7)


# A - Final return value is summation Mod ----
	 # T is max 10, n is max 10^6. Tn = n^2 - (n-1) ^2
# D - Loop until n, Find T at each n, add to overall sum. Divide overall sum by ----
# P
# W
# T

# Examplify
# Pattern Matching
# Base Case and Build
# Simplify and Generalize
# List Data Structures

def sumSeries(n):
	finalSum = 0

	for i in range(n):
		num = i + 1
		t = math.pow(num,2) - math.pow((num-1),2)

		finalSum += t

	return finalSum % (math.pow(10,9) + 7)


# RESULTS - note that T is a telescopic series. Also T simplifies to 2n-1. One line solution : for cas in xrange(input()): print pow(input(), 2, 10**9+7)






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


# print " TESTING "
# print anagrams("the eyes","they see")
# print anagrams("the eyes","they see!")
# print anagrams("the eyes","they do see")
# print anagrams("SCHOOL MASTER","THE CLASSROOM")
# print anagrams("one sentence","a different sentence")


# Dijkstra's shortest path algorithm

# Similar to BFS. Start at a node and iterates through all the nodes to find the shortest path.  

# Graph class that can add nodes and edges with info for distances
class Graph:
	def __init__(self):
		self.nodes = set()
		self.edges = {}
		self.distances = {}


	def add_node(self, value):
		self.nodes.add(value)
		self.edges[value] = []

	def add_edge(self,from_n,to_n,distance):
		self.edges[from_n].append(to_n)
		self.edges[to_n].append(from_n)
		self.distances[(from_n, to_n)] = distance

	def show_nodes(self):
		print self.nodes

	def show_edges(self):
		print self.edges

	def show_distances(self):
		print self.distances

# TESTING
# ng = Graph()
# ng.add_node("a")
# ng.add_node("b")
# ng.add_edge("a", "b", 3)


# Priority Queue implementation with heappq python module
class PriorityQueue():
	def __init__(self):
		self._queue = []
		self._index = 0

	def push(self, item, priority):
		heapq.heappush(self._queue, (-priority, self._index, item))
		self._index += 1

	def pop(self):
		return heapq.heappop(self._queue)[-1]




# DIJKSTRA (G, w, s)

# INITIALIZE SINGLE-SOURCE (G, s)
# S  { }     // S will ultimately contains vertices of final shortest-path weights from s
# Initialize priority queue Q i.e., Q    V[G]
# while priority queue Q  is not empty do
#     u    EXTRACT_MIN(Q)    // Pull out new vertex
#     S    S in {u}
#     // Perform relaxation for each vertex v adjacent to u
#     for each vertex v in Adj[u] do
#         Relax (u, v, w)


# SUBSEQUENCE WEIGHTING
# A subsequence of a sequence is a sequence which is obtained by deleting zero or more elements from the sequence.
# You are given a sequence A in which every element is a pair of integers i.e A = [(a , w ), (a , w ),..., (a , w )].
# For a subseqence B = [(b , v ), (b , v ), ...., (b , v )] of the given sequence :
# We call it increasing if for every i (1 <= i < M ) , b < b .
# Weight(B) = v + v + ... + v .
# Task:
# Given a sequence, output the maximum weight formed by an increasing subsequence.

# Sort the input in O(nlogn) by increasing x values
# Find the max weight in the sorted array

def quick_sort(items):
    
    if len(items) > 1:
        pivot_index = len(items) / 2
        smaller_items = []
        larger_items = []

        for i, val in enumerate(items):
            if i != pivot_index:
                if val < items[pivot_index]:
                    smaller_items.append(val)
                else:
                    larger_items.append(val)

        quick_sort(smaller_items)
        quick_sort(larger_items)
        items[:] = smaller_items + [items[pivot_index]] + larger_items


def subweighting(sortedArr):
	if len(sortedArr) == 1:
		return sortedArr[0][1]
	else:
		return max(sortedArr[len(sortedArr) - 1] + subweighting[sortedArr[:-1]], subweighting[sortedArr[:-1]])





