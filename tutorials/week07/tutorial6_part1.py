"""CSC110 Tutorial 6: Loops and Mutation, Exercise 1

Module Description
==================
This module contains the functions you should complete for Exercise 1. For each one,
you should use a loop with a mutable accumulator and mutating operations to avoid
creating many brand-new objects.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2026 CSC110 Teaching Team
"""
from python_ta.contracts import check_contracts


@check_contracts
def vowel_counts(s: str) -> dict[str, int]:
    """Return a dictionary mapping the five lowercase vowels to the number of times
    each vowel appears in s.

    Uppercase vowels are NOT counted.

    >>> result = vowel_counts('teacher is cool')
    >>> result['a']
    1
    >>> result['e']
    2
    >>> result['i']
    1
    >>> result['o']
    2
    >>> result['u']
    0
    """
    dict_so_far = {'a' : 0, 'e' : 0, 'i' : 0, 'o' : 0, 'u': 0}
    for j in dict_so_far:
        for i in s:
            if i == j:
                    dict_so_far[j] += 1
    return dict_so_far






@check_contracts
def vowel_counts_multiple(strings: set[str]) -> dict[str, int]:
    """Return a dictionary mapping the five lowercase vowels to the number of times
    each vowel appears in the given strings.

    Uppercase vowels are NOT counted.

    >>> result = vowel_counts_multiple({'teacher', 'is', 'cool'})
    >>> result['a']
    1
    >>> result['e']
    2
    >>> result['i']
    1
    >>> result['o']
    2
    >>> result['u']
    0

    NOTE: Do *not* use vowel_counts; instead, use nested loops to implement
    this function (to practice writing code with nested loops). Your implementation
    should look similar to vowel_counts, but with an additional loop added.
    """
    dict_so_far = {'a' : 0, 'e' : 0, 'i' : 0, 'o' : 0, 'u': 0}
    for i in dict_so_far:
         for j in strings:
              for k in j:
                   if k == i:
                        dict_so_far[i] += 1
    return dict_so_far

@check_contracts
def vowel_counts_by_string(strings: set[str]) -> dict[str, dict[str, int]]:
    """Return a mapping from each given string to its vowel count dictionary
    (i.e., what would be returned by vowel_counts when given the string).

    Equivalent to the comprehension

        {string: vowel_counts(string) for string in strings}

    >>> result = vowel_counts_by_string({'teacher', 'is', 'cool'})
    >>> result['teacher'] == {'a': 1, 'e': 2, 'i': 0, 'o': 0, 'u': 0}
    True
    >>> result['is'] == {'a': 0, 'e': 0, 'i': 1, 'o': 0, 'u': 0}
    True
    >>> result['cool'] == {'a': 0, 'e': 0, 'i': 0, 'o': 2, 'u': 0}
    True

    NOTE: Do *not* use vowel_counts; instead, use nested loops to implement
    this function (to practice writing code with nested loops). Your implementation
    should look similar to vowel_counts, but with an additional loop added.
    However, this should *also* be different from vowel_counts_multiple (for this
    function, you'll need a second accumulator variable).
    """
    dict_so_far = {}
    for i in strings:
        vowels_so_far = {'a' : 0, 'e' : 0, 'i' : 0, 'o' : 0, 'u': 0}
        for j in vowels_so_far:
             for k in i:
                  if j == k:
                       vowels_so_far[j] += 1
        dict_so_far[i] = vowels_so_far
    return dict_so_far




if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
