"""Generator Expression Exercises."""
# pylint: disable=unreachable


def sum_all(matrix):
    """Return the sum of all numbers in the given list-of-lists."""
    return sum(sum(x) for x in matrix)

    # Alternative Solution

    return [
        n
        for row in matrix
        for n in row 
    ]

def all_together(*args):
    """String together all items from the given iterables."""
    return (element for iter in args for element in iter )

def interleave(iter1, iter2):
    """Return iterable of one item at a time from each list."""
    return ( element  for pair in zip(iter1,iter2) for element in pair)

def deep_add(iterable_or_number):
    """Return sum of values in given iterable, iterating deeply."""
    if not hasattr(iterable_or_number, '__iter__'):
        return iterable_or_number
    else:
        return sum(deep_add(possible) for possible in  iterable_or_number)
    
def parse_ranges(numbers):
    """Return a list of numbers corresponding to number ranges in a string"""
    interval = (endpoints.split('-') for endpoints in numbers.split(',')) 
    
    return [ 
        number 
        for star, end  in interval 
        for number in range(int(star), int(end)+1)
        ]
    
    # Alternative solution returning a genetaror
    return (
        number
        for to_parse in numbers.split(',')
        for number in range(int(to_parse.split('-')[0]),int(to_parse.split('-')[1])+1) 
    )

def is_prime(candidate):
    """
    Return True if candidate number is prime.
    REWRITE:
    def is_prime(candidate):
    for n in range(2, candidate // 2):
        if candidate % n == 0:
            return False
    return True
    """
    return all(candidate % n != 0 for n in range(2, candidate//2)) 