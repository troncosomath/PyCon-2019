"""Generator Function Exercises."""


def unique(iterable):
    """Yield iterable elements in order, skipping duplicate values."""
    unique_elements = set()
    for element in iterable:
        if element not in unique_elements:
            unique_elements.add(element)
            yield(element)

def float_range(start, end, step=1.0):
    """Return iterable of numbers from start to stop by step."""
    current = start
    while current < end:
        yield current
        current += step


def head(iter, n=0):
    """Return first n items of a given iterable."""
    current = 0
    while current < min(n, len(iter)):
        yield iter[current]
        current +=1

    # Alternative solutuion using for and enumerate
    # for index, value in enumerate(iter):
    #     if index < n:
    #         yield value
    #     else:
    #         break

def pairwise(iterable):
    """
    Yield a tuple containing each item and the item following it.

    The item after the last one is treated as ``None``.
    """
    for i, value in enumerate(iterable):
        
        if i == len(iterable)-1:
            yield (value, None)
        else:
            yield (value, iterable[i+1])

def around(iterable):
    """
    Yield a tuple of the previous, current, and next items.

    The previous item should start at ``None`` and the next item should
    be ``None`` for the last item in the iterable.
    """
    for i in range(len(iterable)):
        edge_left = None if i == 0 else iterable[i-1] 
        edge_right = None if i == len(iterable)-1 else iterable[i+1] 
        
        yield (edge_left, iterable[i], edge_right)


def stop_on(itera, stop):
    """Yield from the iterable until the given value is reached."""
    
    for value in itera:
        if value != stop:
            yield value
        else:
            break

def deep_flatten(iterable_or_number):
    """Flatten an iterable of iterables."""
    try:
        for item in iterable_or_number:
            yield from deep_flatten(item)
    except TypeError:
        yield iterable_or_number

def get_primes_over(number_primes=0):
    """Return given number of primes over 1,000,000."""
    # Naive approach
    count = 0
    def is_prime(p):
        for i in range(2, int(p**0.5)+1):
            if p % i == 0:
                return False
        return True
    
    current = 1_000_000
    while count < number_primes:
        if is_prime(current):
            yield current
            count += 1
        current +=1
        

