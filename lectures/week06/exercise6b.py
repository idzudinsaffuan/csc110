# it only checks for the first character of the str
# it checks only for the last character
# it only checks for the first character of the str

def is_IP_address(address: str) -> bool:
    """
    Return whether address contains only digits and periods.
    """
    for ch in address:
        if ch not in '0123456789.':
            return False
    return True

def all_fluffy(s: str) -> bool:
    """Return whether every character in s is fluffy.

    Fluffy characters are those that appear in the word 'fluffy'.

    >>> all_fluffy('fffffuy')
    True
    >>> all_fluffy('abcfluffy')
    False
    """
    for i in range(len(s)):
        if s[i] not in 'fluffy':
            return False

    return True

def is_sorted(lst: list[int]) -> bool:
    """Return whether lst is sorted.

    A list L is sorted when for every pair of *adjacent* elements
    x and y in L, x <= y.

    lists of length < 2 are always sorted.

    >>> is_sorted([1, 5, 7, 100])
    True
    >>> is_sorted([1, 2, 1, 2, 1])
    False
    """
    for i in range(0, len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True

def inner_product(nums1: list[float], nums2: list[float]) -> float:
    """Return the inner product of nums1 and nums2.

    The inner product of two lists is the sum of the products of the
    corresponding elements of each list:

        sum([nums1[i] * nums2[i] for i in range(0, len(nums1))])

    Preconditions:
        - len(nums1) == len(nums2)

    >>> inner_product([1.0, 2.0, 3.0], [0.5, 2.5, 0.0])
    5.5
    """
    sum_so_far = 0
    for i in range(0, len(nums1)):
        sum_so_far = sum_so_far + nums1[i] * nums2[i]
    return sum_so_far


def stretch_string(s: str, stretch_factors: list[int]) -> str:
    """Return a string consisting of the characters in s, each repeated
    a given number of times.

    Each character in s is repeated n times, where n is the int at the
    corresponding index in stretch_factors.
    For example,
        - s[0] is repeated stretch_factors[0] times
        - s[1] is repeated stretch_factors[1] times
        - etc.

    Preconditions:
        - len(s) == len(stretch_factors)
        - all({factor >= 0 for factor in stretch_factors})

    >>> stretch_string('David', [2, 4, 3, 1, 1])
    'DDaaaavvvid'
    >>> stretch_string('echo', [0, 0, 1, 5])
    'hooooo'
    """
    str_so_far = ''
    for i in range(len(s)):
        str_so_far = str_so_far + s[i] * stretch_factors[i]
    return str_so_far

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

def total_mice(dict_of_cats: dict[str, list[str]]) -> int:
    """Return the number of mice stored in the given cat dictionary.

    dict_of_cats is a dictionary here:
        - Each key is the name of a cat
        - Each corresponding value is a list of items that the cat owns.
          An item is a *mouse* when it contains the string 'mouse'.
          (You can use the "in" operator to check whether one string is
          in another.)

    >>> total_mice({'Romeo': ['mouse 1', 'my fav mouse', 'flower'],
    ...             'Juliet': ['sock', 'mouse for tonight']})
    3
    >>> total_mice({'Asya': ['chocolate', 'toy'], 'Mitzey': []})
    0

    HINT: remember that when iterating over a dictionary, the loop
    variable refers to the *key* of the dictionary. Use key lookup
    (i.e., `dict_of_cats[key]`) to access the corresponding value.
    """
