"""Iterator exercises"""
# pylint: disable=unreachable
import random

def first(iterable):
    """Return the first item in given iterable."""
    for element in iterable:
        return element

    # Alternative solution
    return next(iter(iterable))

def is_iterator(iterable):
    """Return True if given iterable is an iterator."""
    return iter(iterable) is iterable
    
    # The following won't work because we consume an element of t he iterable. 
    try:
        next(iterable)
    except:
        return False
    else:
        return True

class Point:
    """3-D Point objects"""
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __iter__(self):
        for element in (self.x, self.y, self.z):
            yield element

def all_same(to_iterate):
    """Return True if all items in the given iterable are the same."""
    current = next
    to_compare = iter(to_iterate)
    try:
        current = next(to_compare)
    except:
        return True

    for element in to_compare:
        if current != element:
            return False

    return True

def minmax(iterable ):
    """Return minimum and maximum values from given iterable."""
    to_iter = iter(iterable)
    try:
        min_iterable = next(to_iter)
        max_iterable = min_iterable
    except:
        return (None, None)

    for element in to_iter:
        if element < min_iterable:
            min_iterable = element
        if element > max_iterable:
            max_iterable = element

    return (min_iterable, max_iterable)

class RandomNumberGenerator:
    """Return infinite series of randomly generator numbers."""
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        return random.randint(self.start, self.end)
