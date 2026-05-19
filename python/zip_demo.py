# zip_demo.py

#
# zip tricks
#
def zip_tricks():
    A = [1, 2, 3, 4]
    B = [5, 6, 7, 8]
    C = [9, 10, 11, 12]

    # ...

# zip_tricks()

#
# matrices
#
m1 = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
]

m2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def print_matrix(matrix):
    # ...
    pass

def matrix_demo():
    # ...
    pass

#
# How could we use zip to transpose a matrix?
#
# The zip_tricks function shows an answer for a matrix with known dimensions.
#

# assumes matrix is 3 rows, 3 columns
def transpose3(matrix):
    # ...
    pass

#
# Try replacing m2 by m1 in the following code: you'll see that transpose chops
# off some of the result!
#
# print_matrix(m2)
# print()
# print_matrix(transpose3(m2))

#
# Dealing with multiple function arguments.
#
def like(a, b, c):
    print(f'I like {a}, {b}, and {c}.')

def like_demo():
    like(1, 2, 3)
    nums = [4, 5, 6]
    like(nums[0], nums[1], nums[2])
    # ...

# like_demo()

#
# Transposing any matrix with zip
#
def transpose(matrix):
    # ...
    pass

# def transpose_demo():
#     print_matrix(m1)
#     print()
#     print_matrix(transpose(m1))

#     print()
#     print()

#     print_matrix(m2)
#     print()
#     print_matrix(transpose(m2))
