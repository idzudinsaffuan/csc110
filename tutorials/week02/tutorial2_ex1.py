"""CSC110 Tutorial 2: Functions, Logic, and Autocorrecting with Predicates (Exercise 1)

Module Description
==================
Write your functions for Exercise 1 in this file. Note that you're responsible
for the entire function design, following the steps of the Function Design Recipe.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2026 CSC110 Teaching Team
"""
def average_len_str(strings: list) -> float:

    """
    return the average length of strings in a given list of strings, rounded to 2 decimal places.
    return -1.0 if the empty list is given
    >>> average_len_str(['juden', 'is', 'handsome'])
    5.0
    >>> average_len_str(['juden', 'is', 'cool'])
    3.67
    >>> average_len_str([])
    -1.0
    """
    if len(strings) == 0:
        return -1.0
    else:
        total = sum([len(str) for str in strings])
        return round(total / len(strings), 2)

def str_length_less_than_num(strings: set, number: int) -> set:
    """
    >>> sets = str_length_less_than_num({'idzudin', 'is', 'really', 'cool'}, 4)
    >>> sets == {'is','cool'}
    True
    >>> sets = str_length_less_than_num({'idzudin', 'is', 'really', 'cool'}, 6)
    >>> sets == {'is', 'really', 'cool'}
    True
    """

    return {str for str in strings if len(str) <= number}

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
