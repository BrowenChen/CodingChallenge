"""
Swap two numbers with no temporary variable
--------
>>> lst = [1,2,3,4]
>>> swap(lst[1], lst[2])
>>> lst = [1,3,2,4]
"""


lst = [1,2,3,4]

def test():
  return "Hello World"

def noTempSwap(in1, in2, lst):
  x = lst[in1] + lst[in2]
  y = x - lst[in1]
  x -= y

  lst[in1] = y
  lst[in2] = x

  print(lst)

  return lst
