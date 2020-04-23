"""List comprehension exercises"""
# pylint: disable=unreachable


def get_vowel_names(names):
    """Return a list containing all names given that start with a vowel."""
    return [name for name in names if name[0].lower() in "aeiou"]

def flatten(matrix):
    """Return a flattened version of the given 2-D matrix (list-of-lists)."""    
    return [item for row in matrix for item in row ]

def matrix_from_string(s):
    """Convert rows of numbers to list of lists."""
    return [ [int(x) for x in row.split(' ')] for row in s.split("\n")]

def power_list(numbers):
    """Return a list that contains each number raised to the i-th power."""
    
    return [element**index for index, element in enumerate(numbers)]

def matrix_add(matrix1, matrix2):
    """Add corresponding numbers in given 2-D matrices."""
    return [ [a+b for a,b in zip(row1, row2)] for row1, row2 in zip(matrix1, matrix2) ]
   
def identity(x):
    """Return an identity matrix of size x size."""
    return [[1 if i ==j else 0 for j in range(x)] for i in range(x)]


def triples(num):
    """Return list of Pythagorean triples less than input num."""
    return [
        (i , j, int((i**2 + j**2)**0.5) ) 
        for i in range(1,num)
        for j in range(i, num)
        if int((i**2 + j**2)**0.5) < i+j 
        and int((i**2 + j**2)**0.5) < num 
        and int((i**2 + j**2)**0.5)**2 == i**2 + j**2
    ]

    # Alternative Solution 1
    return [
        (a, b, c)
        for a in range(1, num)
        for b in range(a+1, num)
        for c in range(b+1, num)
        if a**2 + b**2 == c**2
    ]
    