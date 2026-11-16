"""CSC110 Tutorial 6: Loops and Mutation, Exercise 2

Module Description
==================
This module contains a set of erroneous functions involving for loops
and/or object mutation.

Follow the handout to call one function at a time from a main block.
Use the VS Code Python debugger to trace each call.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2026 CSC110 Teaching Team
"""


def total_string_size(strings: set[str]) -> int:
    """Return the total length of the given strings.

    >>> total_string_size({'Hello', 'a', 'David is cool'})
    19
    """
    total_size_so_far = 0
    for s in strings:
        total_size_so_far += len(s)
    return total_size_so_far


def has_special(strings: list[str]) -> bool:
    """Return whether there is a special string in the given collection of strings.

    We say that a string is special when it has length >= 2 and it starts and ends
    with the same character.

    >>> has_special(['a', 'bc', 'david'])
    True
    """
    bool_so_far = False
    for s in strings:
        if len(s) >= 2 and s[0] == s[len(s) - 1]:
            bool_so_far = True
        else:
            bool_so_far = bool_so_far or False
    return bool_so_far


def multiples_of_three(n: int) -> list[int]:
    """Return a list containing the numbers between 0 and n - 1 (inclusive) divisible by 3.

    Preconditions:
    - n >= 1

    >>> multiples_of_three(7)
    [0, 3, 6]
    """
    multiples_so_far = []

    for i in range(0, n):
        if i % 3 == 0:
            multiples_so_far.append(i)

    return multiples_so_far


def bonus_score(strings: list[str], bonus_chars: set[str]) -> int:
    """Return the total "bonus score" for the given strings and bonus_chars.

    The "bonus score" is calculated as follows:
        - for each string in strings, calculate the number of characters in
          the string that are also in bonus_chars
        - if this number is >= 3, add the number to the "bonus score"

    Preconditions:
        - all({len(c) == 1 for c in bonus_chars})

    >>> bonus_score(['David', 'Mario', 'Banana', 'CSC110'], {'M', 'a', 'r', 'i', 'o'})
    8
    """
    total_bonus_so_far = 0

    for s in strings:
        string_bonus_so_far = 0
        for char in s:
            if char in bonus_chars:
                string_bonus_so_far = string_bonus_so_far + 1


        if string_bonus_so_far >= 3:
            total_bonus_so_far = total_bonus_so_far + string_bonus_so_far

    return total_bonus_so_far

if __name__ == '__main__':
    print(total_string_size({'Hello', 'a', 'David is cool'}))
