import time

# Question 1: In your own words, explain what a list comprehension is in Python.
# Answer: List comprehension is a single line way to create a list by looping through another list and applying filter
# or mathematical transformation at the same time

# Question 2:
# Make a list of all the numbers from 1 to 100 that are multiples of 5, e.g. [5, 10, 15, ...].
def q1():
    print([x for x in range(5, 101, 5)])

# Remove from a given list all the strings of even length.
def q2b(strs):
    return [s for s in strs
              if len(s) % 2 != 0 ]
            # if len(s) & 1]

# Remove from a given list all the 0s, add 1 to all negative numbers, and subtract 1 from all positive numbers. For instance, [0, 2, -2, 0, -3] becomes [1, -1, -2].
def q2c(strs):
    return  [s+1 if s<0 else s-1
                 for s in strs if s != 0]

# Make a list of all 4-bit tuples, e.g. [(0,0,0,0), (0, 0, 0, 1), (0, 0, 1, 0), ...].
def q2d():
    return [(a, b, c, d) for a in range(2) for b in range(2) for c in range(2) for d in range(2)]

# Given three list, generate all 3-tuples of (a, b, c) where a is from the first list, b is from the second list, c is
# from the third list, and a, b, and c are all different.
def q2e(A, B, C):
    return [(a, b, c) for a in A for b in B for c in C
                if a != b and b != c and a != c]

# Make a list of all integer solutions to the equation a^2 + b^2 = c^2. Assume a, b, and c are all integers between 1
# and 100, and a < b < c. Write each solution as a tuple (a, b, c). The list starts and ends with:
# [(3, 4, 5), (5, 12, 13), (6, 8, 10), ..., (60, 80, 100), (65, 72, 97)].
def q2f():
    return [(a, b, c) for a in range (1, 101)
                      for b in range (1, 101)
                      for c in range (1, 101)
                      if a**2 + b**2 == c**2]

# Question 3: In Python, what is the walrus operator? What is used for? Give an example.
# Answer: Walrus operator is ":=", a syntax trick that allows you to assign value to a variable and evaluate it
# immediately in an expression / filter at the same time.


# Question 4: Using the zip function, write a function called add_lists(A, B) that that adds two lists of numbers
# element-wise. Assume the lists are non-empty, only contain numbers, and have the same length.
# For example, add_lists([1, 2, 3], [4, 5, 6]) should return [5, 7, 9].
def add_lists(A, B):
    return [(a, b) for a, b in zip(A, B)]

# Question 5: Using zip and sum, show how to calculate the dot product of two lists of numbers. Assume the lists are
# non-empty, only contain numbers, and have the same length. For example, the dot product of [1, 2, 3] and [4, 5, 6] is
# 1*4 + 2*5 + 3*6 = 32.
def q5(lst1, lst2):
    return [sum(a*b for a, b in zip(lst1, lst2))]

# Question 6: Given a list of strings, use a loop (or a list comprehension) and enumerate to print each string on its
# own line, numbered starting from 1. For example, if the list is ['apple', 'banana', 'cherry'], the output should be:
# 1. apple 2. banana 3. cherry
def q6(lst):
    print(*(f"{i+1}. {s}" for i, s in enumerate(lst)), sep='\n')

# Question 7: Write a function called get_max(lst) that uses enumerate to return the largest value in the list. Assume
# the list is non-empty and is either all numbers or all strings. For example, get_max([4, 8, 4, 1]) should return 8, and
# get_max(['soap', 'cat', 'dog']) should return 'soap'.
def get_max(lst):
    max = 0
    for i, x in enumerate(lst):
        if x > lst[max]:
            max = i
    return lst[max]

# Question 8: Explain the iterator protocol in Python. What are the methods required? What happens when there is no more
# data to iterate over?
# Answer: Iterator needs __next__() and __iter__(), if not more data then raise StopIteration exception.

# Question 9
class My_reversed:
  def __init__(self, s):
    self.i = len(s)
    self.s = s
  def __iter__(self):
    return self
  def __next__(self):
    if self.i == 0:
      raise StopIteration
    self.i -= 1
    return self.s[self.i]

# q11
class My_enumerate:
  def __init__(self, seq):
    self.i = -1
    self.seq = seq
  def __iter__(self):
    return self
  def __next__(self):
    if self.i == len(self.seq)-1:
      raise StopIteration
    self.i += 1
    return (self.i, self.seq[self.i])

# q11.1
def my_range(a, b):
  while(a < b):
    yield a
    a += 1

def my_zip(A, B):
  for i in range(len(A)):
    yield (A[i], B[i])

# q12
def gen_longer_than(n, lst):
  for s in lst:
    if len(s) > n:
      yield s

# q13
def gen_lines_of(filename):
  with open(filename, 'r') as file:
    for line in file:
      yield line[:-1]

# q14
def make_bounds_checker(min, max):
  def func(val):
    return min <= val < max
  return func

# q15
def make_bad_str_counter(bad_strs):
  def func(str):
    return sum(1 for bad_str in bad_strs if bad_str in str)
  return func

# q17
def always_return_str(func):
  def wrapper(*args, **kwargs):
    return str(func(*args, **kwargs))
  return wrapper
# q6(["a", "b", "c", "d", "e"])

